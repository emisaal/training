from typing import Self

class _Node:
    def __init__(self, data: any, next: any = None) -> None:
        self.data = data
        self.next = next


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

    def __len__(self) -> int:
        """Called to implement the built-in function len()."""
        return self._length

    def _get_positive_index(self, index: int) -> int:
        """Change provided index into a positive index."""
        
        if index < 0:
            index = self._length + index
        return index

    def _find_node(self, index: int) -> _Node | None:
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

    def __getitem__(self, index: int) -> any:
        """Called to implement evaluation of self[key]."""

        if not isinstance(index, int):
            raise TypeError

        node = self._find_node(index)
        return node.data

    def __setitem__(self, index, data) -> None:
        """Called to implement assignment to self[key]."""

        if not isinstance(index, int):
            raise TypeError

        node = self._find_node(index)
        node.data = data

    def __delitem__(self, index: int) -> None:
        """Called to implement deletion of self[key]."""

        if not isinstance(index, int):
            raise TypeError

        if index == -1:
            prev_node = self._find_node(-2)
            prev_node.next = None

        elif index == 0:
            self._first_node = self._first_node.next

        else:
            index = self._get_positive_index(index)
            prev_node = self._find_node(index - 1)
            prev_node.next = prev_node.next.next

        self._length -= 1
        return

    def __iter__(self) -> None:
        """This method is called when an iterator is required for a container."""

        node = self._first_node
        while node is not None:
            yield node.data
            node = node.next

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

        node = self._first_node
        prev_node = self._first_node

        while node is not None:
            if node.data != data:
                prev_node = node
                node = node.next
                continue

            prev_node.next = node.next
            return

        raise ValueError