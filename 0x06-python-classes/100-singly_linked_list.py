#!/usr/bin/python3
"""Class for Node"""


class Node:
    """ defines a node of a singly linked list
        Attributes:
            data (int): data
            next_node (Node, optional): node
    """

    def __init__(self, data, next_node=None):
        """Initialize Node
        args:
            data (int): data stored in node
            next_node (Node): next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter
        returns:
            data (int)
        """
        return self.__data

    @data.setter
    def data(self, value):
        """data setter
        args:
            value (int): value to set
        returns:
            None
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """data getter
        returns:
            data (int)
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """data setter
        args:
            value (Node): value to set
        returns:
            None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class
    """

    def __init__(self):
        """Initialize linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """insert node in coorect sorted position
        args:
            value (int): value for new node
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node

            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
