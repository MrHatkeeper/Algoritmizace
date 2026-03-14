from itertools import count


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
        nNode = Node(data)
        nNode.next = self.head
        self.head = nNode

    def display(self):
        for x in self:
            print(x, end=" -> ")
        print(".")

    def display1(self):
        actNode = self.head
        while actNode != self.endnode:
            print(actNode, end=" -> ")
            actNode = actNode.next
        print(".")

    def __str__(self) -> str:
        """Converts the LinkedList to string (for print): lists data from all nodes in the linked list."""
        actNode = self.head
        s = "{"
        while actNode != self.endnode:
            s += f"{actNode}"
            if actNode.next != self.endnode:
                s += " -> "
            actNode = actNode.next
        s = s + "}"
        return s

    def delete_all(self):
        """Deletes all nodes from the linked list (except the sentinel node)."""
        actNode = self.head
        while actNode != self.endnode:
            self.head = actNode.next
            del actNode
            actNode = self.head

    def find(self, data) -> Node | None:
        """
        Finds the first occurrence of a node with the specified data in the linked list.

        Returns:
            - The first node containing the specified data, if found.
            - None if no matching node is found.
        """
        actNode = self.head
        while actNode != self.endnode:
            if actNode.data == data:
                return actNode
            actNode = actNode.next
        return None

    def first(self):
        """
        Returns the data stored in the first node of the linked list.

        Raises:
            ValueError: If the linked list is empty.
        """
        if self.is_empty():
            raise ValueError("The linked list is empty")
        return self.head.data

    def last(self):
        """
        Returns the data stored in the last node of the linked list (the node before the sentinel node).

        Raises:
            ValueError: If the linked list is empty.
        """
        if self.is_empty():
            raise ValueError("The linked list is empty")
        actNode = self.head
        while actNode != self.endnode:
            if actNode.next == self.endnode:
                return actNode.data
            actNode = actNode.next

    def remove_first(self):
        """
        Removes the first node of the linked list and returns the data from it.

        Raises:
            ValueError: If the linked list is empty.
        """
        if self.is_empty():
            raise ValueError("The linked list is empty")
        holder = self.head.next
        output = self.head.data
        del self.head
        self.head = holder
        return output

    def remove_last(self):
        """
        Removes the last node of the linked list and returns the data from it.

        Raises:
            ValueError: If the linked list is empty.
        """
        if self.is_empty():
            raise ValueError("The linked list is empty")
        actNode = self.head
        while actNode != self.endnode:
            if actNode.next.next == self.endnode:
                output = actNode.next.data
                del actNode.next
                actNode.next = self.endnode
                return output
            actNode = actNode.next

    def delete(self, data):
        """
        Deletes the first occurrence of a node with the specified data from the linked list.

        Returns:
            bool: True if a node was deleted, False if the data was not found.
        """
        actNode = self.head
        prevNode = None
        while actNode != self.endnode:
            nextNode = actNode.next
            if actNode.data == data:
                if actNode == self.head:
                    self.head = nextNode
                if prevNode is not None:
                    prevNode.next = nextNode
                del actNode
                return True
            prevNode = actNode
            actNode = nextNode
        return False

    def delete_all_occurrences(self, data):
        """
        Deletes all nodes with the specified data from the linked list.

        Returns:
            int: The number of deleted nodes.
        """
        actNode = self.head
        prevNode = None
        counter = 0
        while actNode != self.endnode:
            nextNode = actNode.next
            if actNode.data == data:
                if actNode == self.head:
                    self.head = nextNode
                if prevNode is not None:
                    prevNode.next = nextNode
                del actNode
                actNode = prevNode
                counter +=1
            prevNode = actNode
            actNode = nextNode
        return counter

    def __getitem__(self, index: int):
        """
        Returns the data stored at the specified index (0-based).

        Raises:
            IndexError: If the index is out of range.
        """
        actNode = self.head
        i = 0
        while actNode != self.endnode:
            if i == index:
                return actNode.data
            i += 1
            actNode = actNode.next
        raise IndexError("Index out of range")

    def __setitem__(self, index: int, data):
        """
        Sets the data at the specified index (0-based).

        Raises:
            IndexError: If the index is out of range.
        """
        actNode = self.head
        i = 0
        while actNode != self.endnode:
            if i == index:
                actNode.data = data
                return
            i += 1
            actNode = actNode.next
        raise IndexError("Index out of range")

    def __iter__(self):
        """
        Returns a Python iterator for the linked list.
        """
        actNode = self.head
        while actNode != self.endnode:
            yield actNode.data
            actNode = actNode.next
        # return LinkedListIterator(self.head, self.endnode)

    def find_iter(self, data) -> "PositionIterator":
        """
        Returns an iterator pointing to the first occurrence of the specified data.
        """
        actNode = self.head
        while actNode != self.endnode:
            if actNode.data == data:
                return PositionIterator(self, actNode)
        return PositionIterator(self, self.endnode)

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
        self.actNode = head
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
        if self.actNode == self.endnode:
            raise StopIteration()
        data = self.actNode.data
        self.actNode = self.actNode.next
        return data


class PositionIterator:
    """Custom STL-like iterator representing a position inside the linked list."""

    def __init__(self, linked_list, node: Node):
        """
        Initializes the iterator with a reference to the linked list and a node representing the current position.
        """
        self.linked_list = linked_list
        self.actNode = node

    def __eq__(self, __value: object):
        """Checks whether two iterators represent the same position."""
        return isinstance(__value,
                          PositionIterator) and self.linked_list == __value.linked_list and self.actNode == __value.actNode

    def get_value(self):
        """Returns the value stored at the current iterator position.

           Raises:
               ValueError: If the iterator points to the sentinel node (endnode).
        """
        if self.actNode == self.linked_list.endnode:
            raise ValueError()
        return self.actNode.data

    def set_value(self, data):
        """Sets the value at the current iterator position.

           Raises:
               ValueError: If the iterator points to the sentinel node (endnode).
        """
        if self.actNode == self.linked_list.endnode:
            raise ValueError()
        self.actNode.data = data

    def move_to_next(self):
        """Moves the iterator to the next position in the linked list.

        Raises:
               ValueError: If the iterator points to the sentinel node (endnode).
        """
        if self.actNode == self.linked_list.endnode:
            raise ValueError()
        self.actNode = self.actNode.next


if __name__ == "__main__":
    lst = LinkedList()
    for i in range(10):
        lst.append(i)
    print(lst)
    print(f"first: {lst.first()}")
    lst.remove_first()
    print(f"removed first: {lst}")
    print(f"last: {lst.last()}")
    lst.remove_last()
    print(f"removed last: {lst}")
    print(f"find 5: {lst.find(5)}")
    print(f"find last: {lst.find(lst.last())}")
    print(f"find first: {lst.find(lst.first())}")
    print(f"find a: {lst.find("a")}")
    lst.delete(2)
    print(f"delete 2: {lst}")
    lst.delete(lst.first())
    print(f"delete first: {lst}")
    lst.delete(lst.last())
    print(f"delete last: {lst}")

    emptyLst = LinkedList()
    """Testy pro prázdný list. Odkomentované vyhazují error, jelikož jsou prázdné a podle zadání mají vracet error.

    print(f"empty list removed first: {emptyLst}")
    print(f"empty list first: {emptyLst.first()}")
    print(f"empty list last: {emptyLst.last()}")
    emptyLst.remove_first()
    print(f"empty list remove first: {emptyLst}")
    emptyLst.remove_last()
    print(f"empty list remove last: {emptyLst}")"""
    print(f"empty list find a: {emptyLst.find("a")}")
    print(f"empty list delete a: {emptyLst.delete("a")}")
    print(lst)
    print(lst.remove_first())
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