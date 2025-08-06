from typing import Self

class _Node:
    def __init__(self, data: any, next: any = None) -> None:
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class List:
    def __init__(self, args: any = None) -> None:
        self._first_node = None
        self._length = 0

        if args is None:
            return

        self._length += len(args)

        for data in args:
            if self._first_node is None:
                self._first_node = _Node(data)
                curr_node = self._first_node
                continue

            next_node = _Node(data)
            curr_node.next = next_node
            curr_node = next_node

    def __str__(self) -> str:
        return f"[{', '.join(str(data) for data in self)}]"

    def __repr__(self) -> str:
        return f"[{', '.join(str(data) for data in self)}]"

    def __len__(self) -> int:
        """Called to implement the built-in function len()."""
        return self._length

    def _reverse(self, node):
        """"""

        reversed_string = str(node.data)

        if node.next is not None:
            return self._reverse(node.next)  + ', '+  reversed_string
        return reversed_string  # last node

    def _get_reversed_list(self):
        return self._reverse(node=self._first_node)

    def _get_positive_index(self, index: int) -> int:
        """Change provided index into a positive index."""

        return self._length + index if index < 0 else index

    def _find_node(self, index: int = None) -> _Node | None:
        """Find _Node object based on provided index."""

        if self._first_node is None:
            raise IndexError

        index = self._get_positive_index(index)
        node = self._first_node
        idx = 0

        while node is not None:
            if idx == index:
                return node

            node = node.next
            idx += 1

        raise IndexError

    def _remove_item(self, index: int | None = None, data: any = '') -> any:
        """Remove item based on provided index or data."""

        if index is not None:
            if not isinstance(index, int):
                raise TypeError

            if index == 0:
                out_data = self._first_node.data
                self._first_node = self._first_node.next
                self._length -= 1
                return out_data

            index = self._get_positive_index(index)
            prev_node = self._find_node(index - 1)
            out_data = prev_node.next.data

            if index == self._length - 1:
                prev_node.next = None
            else:
                prev_node.next = prev_node.next.next

            self._length -= 1
            return out_data

        if data != '':
            node = self._first_node
            prev_node = self._first_node

            while node is not None:
                if node.data != data:
                    prev_node = node
                    node = node.next
                    continue

                prev_node.next = node.next
                self._length -= 1
                return node.data

            raise ValueError

    def _get_start_stop_step(self, index: slice) -> tuple:
        """"""
        
        start_idx = 0
        stop_idx = self._get_positive_index(-1)
        step = 1 if index.step is None else index.step

        if index.start is not None:
            start_idx = self._get_positive_index(index.start)

        if index.stop is not None:
            stop_idx = self._get_positive_index(index.stop)

        return start_idx, stop_idx, step

    def __getitem__(self, index: int | slice) -> any:
        """Called to implement evaluation of self[key]."""

        if isinstance(index, int):
            node = self._find_node(index)
            return node.data

        elif isinstance(index, slice):
            start_idx, stop_idx, step = self._get_start_stop_step(index)
            out_data = ''
            idx = 0

            if stop_idx == 0 or start_idx >= self._length:
                return '[]'

            for node_data in self:
                if idx >= start_idx:
                    out_data += f'{str(node_data)}'
                else:
                    idx += 1
                    continue

                if idx >= stop_idx:
                    return f'[{out_data}]'
                idx += 1
                out_data += f', '

        raise TypeError

    def __setitem__(self, index, data) -> None:
        """Called to implement assignment to self[key]."""

        if not isinstance(index, int):
            raise TypeError

        node = self._find_node(index)
        node.data = data

    def __delitem__(self, index: int) -> None:
        """Called to implement deletion of self[key]."""

        self._remove_item(index=index)

    def __contains__(self, item: any) -> bool:
        """Called to implement membership test operators."""

        if self.count(data=item) > 0:
            return True
        return False

    def __iter__(self) -> None:
        """This method is called when an iterator is required for a container."""

        node = self._first_node
        while node is not None:
            yield node.data
            node = node.next

    def __reversed___(self) -> None:
        pass

    def append(self, data: any) -> None:
        """Add an item to the end of the list."""

        self.insert(-1, data)
    
    def extend(self, args) -> None:
        """Extend the list by appending all the items from the iterable."""

        for data in args:
            self.append(data)

    def insert(self, index: int, data: any) -> None:
        """Insert an item at a given position."""

        if not isinstance(index, int):
            raise TypeError

        index = self._get_positive_index(index)

        node = self._find_node(index)
        new_node = _Node(data)

        if index == self._length - 1:
            node.next = new_node

        elif index == 0:
            new_node.next = self._first_node
            self._first_node = new_node

        else:
            new_node.next = node
            prev_node = self._find_node(index - 1)
            prev_node.next = new_node

        self._length += 1
        return

    def remove(self, data: any) -> None:
        """Remove the first item from the list whose value is equal to data."""

        self._remove_item(data=data)

    def pop(self, index: int = -1) -> any:
        """Remove the item at the given position in the list, and return it."""

        data = self._remove_item(index=index)
        return data

    def clear(self) -> None:
        """Remove all items from the list."""

        self._first_node = None
        self._length = 0

    def count(self, data: any) -> int:
        """Return the number of times x appears in the list."""

        count = 0
        for node_data in self:
            if node_data == data:
                count += 1
 
        return count
