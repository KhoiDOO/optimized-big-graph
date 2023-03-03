import os
import sys

sys.path.append(os.getcwd())
sys.path.append(os.pardir(os.getcwd()))
from graph.ds_sup.Node.node import Node
from hash_table.hash_table import HashTable
from ctypes import *


class DynamicArray:
    def __init__(self) -> None:
        self.count = 0
        self.capacity = 1
        self.array = self._make_array(self.capacity)

    def __len__(self):
        return self.count

    def _check_index(self, index):
        if index is None:
            raise Exception("index cannot be None")
        elif not isinstance(index, int):
            raise Exception(f"index must be an integer but found {type(index)} instead")
        elif not 0 <= index < self.count:
            return IndexError('K is out of bounds !')

    @staticmethod
    def _check_node(node):
        if node is None:
            raise Exception("node cannot be None")
        elif not isinstance(node, Node):
            raise Exception(f"node must be an integer but found {type(node)} instead")

    @staticmethod
    def _check_capacity(capacity):
        if capacity is None:
            raise Exception("capacity cannot be None")
        elif not isinstance(capacity, int):
            raise Exception(f"capacity must be an integer but found {type(capacity)} instead")

    def __getitem__(self, index: int = None) -> Node:
        self._check_index(index)

        return self.array[index]

    def __setitem__(self, index: int = None, node: Node = None):
        self._check_index(index)

        self.array[index] = node

    def append(self, node: Node = None):
        self._check_node(node)

        if self.count == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.count] = node
        self.count += 1

    def _resize(self, capacity: int = None):
        self._check_capacity(capacity)

        sub_arr = self._make_array(capacity)

        for k in range(self.count):
            sub_arr[k] = self.array[k]

        self.array = sub_arr
        self.capacity = capacity

    def _make_array(self, capacity: int = None) -> py_object():
        self._check_capacity(capacity)

        return (capacity * py_object)()

    def insert_at(self, node: Node = None, index: int = None):
        self._check_node(node)
        self._check_index(index)

        if self.count == self.capacity:
            self._resize(2 * self.capacity)

        for idx in range(self.count - 1, index - 1, -1):
            self.array[idx + 1] = self.array[idx]

        self.array[index] = node
        self.count += 1

    def delete(self):
        if self.count == 0:
            raise Exception("The array is empty. Cannot delete")

        self.array[self.count - 1] = 0
        self.count -= 1

    def remove_at(self, index: int = None):
        if self.count == 0:
            raise Exception("The array is empty. Cannot delete")

        self._check_index(index)

        if index == self.count - 1:
            self.array[index] = 0
            self.count -= 1
            return

        for idx in range(index, self.count - 1):
            self.array[idx] = self.array[idx + 1]

        self.array[self.count - 1] = 0
        self.count -= 1

    def pop(self) -> Node:
        if self.count == 0:
            raise Exception("The array is empty. Cannot pop")

        pop_value = self.array[0]

        self.remove_at(index=0)

        return pop_value

    def show(self):
        for index in range(self.count):
            print(self.array[index].getvalue(), end=" ")
        print()
    
    def _sort_dict(self):
        self.sort_dict = HashTable(capacity=3)
        self.sort_dict["merge"] = self._merge_sort
        self.sort_dict["quick"] = self._quick_sort
        self.sort_dict["tim"] = self._tim_sort

    def sort(self, ascending:bool = False, algo="merge"):
        self.array = self.sort_dict[algo](ascending)


    def _merge_sort(self, ascending:bool = False) -> py_object():
        raise NotImplementedError
    
    def _quick_sort(self, ascending:bool = False) -> py_object():
        raise NotImplementedError
    
    def _tim_sort(self, ascending: bool = False) -> py_object():
        raise NotImplementedError
