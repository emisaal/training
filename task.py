from typing import Self


class List:
    first_node = None

    def __init__(self, *args) -> None:
        self.prev_node = None

        for index, data in enumerate(args):
            if index == 0:
                self.first_node = Node(data, index)
                self.prev_node = self.first_node
                continue

            curr_node = Node(data, index)
            self.prev_node.assign_next_node(curr_node)
            self.prev_node = curr_node

    def __str__(self) -> str:
        return f'[{self.first_node}]'


class Node:
    data = None
    next_node = None
    index = None

    def __init__(self, data: any, index: int) -> None:
        self.data = data
        self.index = index

    def assign_data(self, data: any) -> None:
        self.data = data

    def assign_next_node(self, next_node: Self) -> None:
        self.next_node = next_node

    def __str__(self) -> str:
        return_str = f'{self.data}'
        if self.next_node is not None:
            return_str += f', {self.next_node}'
        return return_str

