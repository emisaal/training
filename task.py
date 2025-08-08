from typing import Self, Generator


class _Node:
    def __init__(self, data: any, next: Self | None = None, prev: Self | None = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class List:
    def __init__(self, args: any = None) -> None:
        self._first_node = None
        self._last_node = None
        self._length = 0

        if args is None:
            return

        if not isinstance(args, tuple):
            self._first_node = self._last_node = _Node(data=args)
            self._length = 1
            return

        self._length += len(args)
        node = None

        for data in args:
            if self._first_node is None:
                self._first_node = node = _Node(data=data)
                continue

            node.next = next_node = _Node(data=data, prev=node)
            node = next_node

        self._last_node = node

    def __repr__(self) -> str:
        return f"[{', '.join(f'{data!r}' for data in self)}]"

    def __len__(self) -> int:
        """Called to implement the built-in function len()."""
        return self._length
    
    def __eq__(self, item: Self) -> bool:
        return str(self) == str(item)

    def __add__(self, item: Self) -> Self:
        """Add two lists."""
        new_list = List()

        for node in self:
            new_list.append(node)
        
        for node in item:
            new_list.append(node)

        return new_list

    def __mul__(self, num: int) -> Self:
        new_list = List()
        
        for _ in range(num):
            for node in self:
                new_list.append(node)

        return new_list

    def _get_positive_index(self, index: int) -> int:
        """Change provided index into a positive index."""

        return self._length + index if index < 0 else index

    def _find_node(self, index: int = None) -> _Node | None:
        """Find _Node object based on provided index."""

        if self._first_node is None:
            raise IndexError

        index = self._get_positive_index(index)

        last = index > self._length / 2
        idx = self._length - 1 if last else 0

        for node in self._node_iter(last):
            if idx == index:
                return node
            idx += -1 if last else 1

        raise IndexError

    def _remove_node(self, node: _Node):
        """Remove provided node."""

        match node:
            case self._first_node:
                self._first_node = node.next
                self._first_node.prev = None

            case self._last_node:
                self._last_node = node.prev
                self._last_node.next = None

            case _:
                node.prev.next = node.next
                node.next.prev = node.prev

        self._length -= 1

    def __getitem__(self, index: int | slice) -> any:
        """Called to implement evaluation of self[key]."""

        if isinstance(index, int):
            return self._find_node(index).data

        elif isinstance(index, slice):
            out_list = List()
            start, stop, step = index.indices(self._length)

            if stop == 0:
                return out_list
            
            idx = 0
            for node in self._node_iter():
                if node is None or idx >= stop:
                    return out_list

                if idx >= start and (idx - start) % step == 0:
                    out_list.append(node.data)

                idx += 1

            return out_list

        raise TypeError

    def __setitem__(self, index: int | slice, data: any) -> None:
        """Called to implement assignment to self[key]."""

        if isinstance(index, int):
            if index == self._length:
                self.insert(-1, data)

            node = self._find_node(index)
            node.data = data
            return

        if not isinstance(index, slice):
            raise TypeError

        if index.start >= self._length - 1:
            for item in data:
                self.insert(self._length, item)
            return

        start, stop, step = index.indices(self._length)

        idx = 0
        data_idx = 0

        for node in self._node_iter():
            if idx > stop or data_idx > len(data) - 1:
                return
            if start <= idx <= stop:
                node.data = data[data_idx]
                data_idx += 1

            idx += 1

    def __delitem__(self, index: int) -> None:
        """Called to implement deletion of self[key]."""

        if not isinstance(index, int):
            raise TypeError

        node = self._find_node(index)
        self._remove_node(node)

    def __contains__(self, data: any) -> bool:
        """Called to implement membership test operators."""

        return any(node_data == data for node_data in self)

    def _node_iter(self, last: bool = False) -> Generator:
        """Iterate nodes."""
        node = self._last_node if last else self._first_node
        while node is not None:
            yield node
            node = node.prev if last else node.next

    def __iter__(self) -> Generator:
        """This method is called when an iterator is required for a container."""

        for node in self._node_iter():
            yield node.data

    def __reversed___(self) -> Generator:
        """Called (if present) by the reversed() built-in to implement reverse iteration."""
        for node in self._node_iter(last=True):
            yield node.data

    def append(self, data: any) -> None:
        """Add an item to the end of the list."""

        self.insert(self._length, data)
    
    def extend(self, args) -> None:
        """Extend the list by appending all the items from the iterable."""

        for data in args:
            self.append(data)

    def insert(self, index: int, data: any) -> None:
        """Insert an item at a given position."""

        if not isinstance(index, int):
            raise TypeError

        if self._first_node is None:
            self._first_node = _Node(data=data)
            self._length = 1
            return

        if index < - 1:
            index = self._get_positive_index(index)

        if index >= self._length:
            index = self._length - 1

        new_node = _Node(data=data)
        node = self._find_node(index)

        # insert as last node in the list
        if index == self._length - 1:
            node.next = new_node
            new_node.prev = node
            self._last_node = new_node

        # insert as the first element
        elif index == 0:
            new_node.next = self._first_node
            self._first_node.prev = new_node
            self._first_node = new_node

        # insert in the middle of the list
        else:
            node.prev.next = new_node

            new_node.next = node
            new_node.prev = node.prev

            node.prev = new_node

        self._length += 1
        return

    def remove(self, data: any) -> None:
        """Remove the first item from the list whose value is equal to data."""

        for node in self._node_iter():
            if node.data != data:
                continue

            self._remove_node(node)
            return node.data

        raise ValueError

    def pop(self, index: int = -1) -> any:
        """Remove the item at the given position in the list, and return it."""

        if not isinstance(index, int):
            raise TypeError

        node = self._find_node(index)
        self._remove_node(node)

        return node.data

    def clear(self) -> None:
        """Remove all items from the list."""

        self._first_node = None
        self._last_node = None
        self._length = 0

    def index(self, data: any, start: int = 0, stop: int = -1):
        """Return zero-based index in the list of the first item whose value is equal to x."""

        idx = 0
        start, stop = self._get_positive_index(start), self._get_positive_index(stop)

        for node_data in self:
            if idx < start:
                idx += 1
                continue
            if idx > stop:
                break
            if node_data == data:
                return idx
            idx += 1

        raise ValueError

    def count(self, data: any) -> int:
        """Return the number of times x appears in the list."""

        count = 0
        for node_data in self:
            if node_data == data:
                count += 1
 
        return count
    
    def reverse(self):
        """Reverse the elements of the list in place."""

        prev_node = None

        for node in self._node_iter(last=True):
            if prev_node is None:
                self._first_node = prev_node = node
                continue

            prev_node.next = node
            prev_node = node

        self._first_node.prev = None

        self._last_node = prev_node
        self._last_node.next = None

    def copy(self):
        new_list = List()
        for node in self:
            new_list.append(node)
        return new_list
