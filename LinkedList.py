class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data=None):
        self.data = data  # Data contained within the node
        self.next = None  # Reference to the next node

    # alternatively: def __init__(self, data = None, next = None):

    def __str__(self) -> str:
        """Returns the string representation of the node (for printing)."""
        return str(self.data)


class LinkedList:
    """Represents a singly linked list with a sentinel node at the end (endnode).

    The sentinel node does not contain meaningful data and serves as a marker for the end of the list.


    The list supports two types of iterators:
    - LinkedListIterator (Python-style traversal)
    - PositionIterator (STL-like position representation)
    """

    def __init__(self):
        """Initializes an empty single linked list with a sentinel node (endnode)."""
        self.endnode = Node()
        self.head = self.endnode

    def is_empty(self) -> bool:
        """Returns True if the linked list is empty (i.e., contains only the sentinel node), False otherwise.
        """
        return self.head == self.endnode

    def append(self, data):
        """Appends a new node with the given data to the end of the linked list."""
        self.endnode.data = data
        new_node = Node(None)
        self.endnode.next = new_node
        self.endnode = new_node

    def insert_at_beginning(self, data):
        """Inserts a new node with the given data at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        for x in self:
            print(x, end=" -> ")
        print(".")

    def display1(self):
        actual_node = self.head
        while actual_node != self.endnode:
            print(actual_node, end=" -> ")
            actual_node = actual_node.next
        print(".")

    def __str__(self) -> str:
        """Converts the LinkedList to string (for print): lists data from all nodes in the linked list."""
        actual_node = self.head
        s = "{"
        while actual_node != self.endnode:
            s += f"{actual_node}"
            if actual_node.next != self.endnode:
                s += " -> "
            actual_node = actual_node.next
        s = s + "}"
        return s

    def delete_all(self):
        """Deletes all nodes from the linked list (except the sentinel node)."""
        ...

    def find(self, data) -> Node:
        """
        Finds the first occurrence of a node with the specified data in the linked list.

        Returns:
            - The first node containing the specified data, if found.
            - None if no matching node is found.
        """
        ...

    def first(self):
        """
        Returns the data stored in the first node of the linked list.

        Raises:
            ValueError: If the linked list is empty.
        """
        return self.head.data

    def last(self):
        """
        Returns the data stored in the last node of the linked list (the node before the sentinel node).

        Raises:
            ValueError: If the linked list is empty.
        """
        ...

    def remove_first(self):
        """
        Removes the first node of the linked list and returns the data from it.

        Raises:
            ValueError: If the linked list is empty.
        """
        ...

    def remove_last(self):
        """
        Removes the last node of the linked list and returns the data from it.

        Raises:
            ValueError: If the linked list is empty.
        """
        ...

    def delete(self, data):
        """
        Deletes the first occurrence of a node with the specified data from the linked list.

        Returns:
            bool: True if a node was deleted, False if the data was not found.
        """
        ...

    def delete_all_occurrences(self, data):
        """
        Deletes all nodes with the specified data from the linked list.

        Returns:
            int: The number of deleted nodes.
        """
        ...

    def __getitem__(self, index: int):
        """
        Returns the data stored at the specified index (0-based).

        Raises:
            IndexError: If the index is out of range.
        """
        actual_node = self.head
        i = 0
        while actual_node != self.endnode:
            if i == index:
                return actual_node.data
            i += 1
            actual_node = actual_node.next
        raise IndexError("Index out of range")

    def __setitem__(self, index: int, data):
        """
        Sets the data at the specified index (0-based).

        Raises:
            IndexError: If the index is out of range.
        """
        actual_node = self.head
        i = 0
        while actual_node != self.endnode:
            if i == index:
                actual_node.data = data
                return
            i += 1
            actual_node = actual_node.next
        raise IndexError("Index out of range")

    def __iter__(self):
        """
        Returns a Python iterator for the linked list.
        """
        actual_node = self.head
        while actual_node != self.endnode:
            yield actual_node.data
            actual_node = actual_node.next
        # return LinkedListIterator(self.head, self.endnode)

    def find_iter(self, data) -> "PositionIterator":
        """
        Returns an iterator pointing to the first occurrence of the specified data.
        """
        actual_node = self.head
        while actual_node != self.endnode:
            if actual_node.data == data:
                return PositionIterator(self, actual_node)
        return PositionIterator(self, endnode)

    def start_iter(self) -> "PositionIterator":
        """
        Returns an iterator pointing to the first element of the list.
        """
        return PositionIterator(self, self.head)

    def end_iter(self) -> "PositionIterator":
        """
        Returns an iterator pointing to the sentinel node (endnode).
        """
        return PositionIterator(self, self.endnode)


class LinkedListIterator:
    """
    Python-style iterator for the LinkedList class.

    This iterator follows the Python iterator protocol and is used in for-loops
    """

    def __init__(self, head: Node, endnode: Node):
        """
        Initializes the iterator with the starting node and the sentinel node (endnode) marking the end of the list.
        """
        self.actual_node = head
        self.endnode = endnode

    def __iter__(self):
        """ Returns the iterator object itself (required by the iterator protocol)."""
        return self

    def __next__(self):
        """
        Returns the next data element in the list.

        Raises:
            StopIteration: If the iterator reaches the sentinel node (endnode).
        """
        if self.actual_node == self.endnode:
            raise StopIteration()
        data = self.actual_node.data
        self.actual_node = self.actual_node.next
        return data


class PositionIterator:
    """Custom STL-like iterator representing a position inside the linked list."""

    def __init__(self, linked_list, node: Node):
        """
        Initializes the iterator with a reference to the linked list and a node representing the current position.
        """
        self.linked_list = linked_list
        self.actual_node = node

    def __eq__(self, __value: object):
        """Checks whether two iterators represent the same position."""
        return isinstance(__value,
                          PositionIterator) and self.linked_list == __value.linked_list and self.actual_node == __value.actual_node

    def get_value(self):
        """Returns the value stored at the current iterator position.

           Raises:
               ValueError: If the iterator points to the sentinel node (endnode).
        """
        if self.actual_node == self.linked_list.endnode:
            raise ValueError()
        return self.actual_node.data

    def set_value(self, data):
        """Sets the value at the current iterator position.

           Raises:
               ValueError: If the iterator points to the sentinel node (endnode).
        """
        if self.actual_node == self.linked_list.endnode:
            raise ValueError()
        self.actual_node.data = data

    def move_to_next(self):
        """Moves the iterator to the next position in the linked list.

        Raises:
               ValueError: If the iterator points to the sentinel node (endnode).
        """
        if self.actual_node == self.linked_list.endnode:
            raise ValueError()
        self.actual_node = self.actual_node.next


if __name__ == "__main__":
    node = Node("A")
    lst = LinkedList()
    print(lst, lst.is_empty())
    for i in range(10):
        lst.append(i)
    print(lst)


def t():
    s = [1, 2, 3]
    it = iter(s)
    print(next(it))
    print(next(it))
    print(next(it))
    for x in s:
        x += 7
    print(s)