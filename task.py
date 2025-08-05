from typing import Self

class Node:
    def __init__(self, data: any, next: any = None):
        self.data = data
        self.next = next


class List:
    def __init__(self, args: any = None):
        self._first_node = None
        self._lenght = 0

        if args is None:
            return

        for data in args:
            self._lenght += 1
            if self._first_node is None:
                self._first_node = Node(data)
                curr_node = self._first_node
                continue

            next_node = Node(data)
            curr_node.next = next_node
            curr_node = next_node

    def __str__(self) -> str:
        return '[' + ', '.join(f'{data}' for data in self.__iter__()) + ']'

    def __len__(self) -> int:
        """Called to implement the built-in function len()."""
        return self._lenght

    def _find_node(self, index: int) -> Node | None:
        """Find Node object based on provided index."""

        if self._first_node is None:
            raise IndexError

        if index < 0:
            index = self._lenght + index

        node = self._first_node
        idx = 0

        while node.next is not None:
            if idx == index:
                break
            node = node.next
            idx += 1

        if idx == index:
            return node
        raise IndexError

    def __getitem__(self, index: int) -> any:
        """Called to implement evaluation of self[key]."""

        if not isinstance(index, int):
            raise TypeError

        node = self._find_node(index)
        return node.data

    def __setitem__(self, index, data):
        """Called to implement assignment to self[key]."""

        if not isinstance(index, int):
            raise TypeError

        node = self._find_node(index)
        node.data = data

    def __delitem__(self, index: int):
        """Called to implement deletion of self[key]."""

        if not isinstance(index, int):
            raise TypeError

        if index == -1:
            prev_node = self._find_node(-2)
            prev_node.next = None

        elif index == 0:
            self._first_node = self._first_node.next

        else:
            if index < 0:
                index = self._lenght + index

            prev_node = self._find_node(index - 1)
            prev_node.next = prev_node.next.next

        self._lenght -= 1
        return

    def __iter__(self):
        """This method is called when an iterator is required for a container."""

        node = self._first_node
        while node is not None:
            yield node.data
            node = node.next

    def append(self, data: any):
        """Add an item to the end of the list."""

        self.insert(-1, data)
    
    def extend(self, args):
        """Extend the list by appending all the items from the iterable."""

        for data in args:
            self.append(data)

    def insert(self, index: int, data: any):
        """Insert an item at a given position."""

        if not isinstance(index, int):
            raise TypeError

        new_node = Node(data)
        node = self._find_node(index)
        if index == -1 or index == self._lenght -1:
            node.next = new_node

        if index == 0:
            new_node.next = self._first_node
            self._first_node = new_node

        self._lenght += 1
