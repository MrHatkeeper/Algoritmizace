class Node:
    """Represents a node in a binary search tree."""

    def __init__(self, data=None):
        self.data = data    # Data contained within the node
        self.left = None    # Reference to the left child Node
        self.right = None   # Reference to the right child Node

    def __str__(self) -> str:
        """Return string representation of the node."""
        return str(self.data)

class BinarySearchTree:
    """
    Represents a Binary Search Tree.
    
    For every node:
    left subtree values < node.data < right subtree values
    """

    def __init__(self):
        """Initializes an empty binary search tree."""
        self.root = None   # Reference to the root node

    def is_empty(self) -> bool:
        """Returns True if the BST is empty, False otherwise."""
        return self.root is None

    def find(self, data):
        """
        Search for a node with the given data. Implement without recursion.

        Parameters:
            data: Data to search for.

        Returns:
            Node with the given data if found, otherwise None.
        """
        actNode = self.root
        while actNode is not None:
            if actNode.data == data:
                return actNode
            if actNode.left is not None and data < actNode.data:
                actNode = actNode.left
            elif actNode.right is not None and data > actNode.data:
                actNode = actNode.right
            else:
                return None
        return None

    def recursive_find(self, data):
        """
        Search for a node with the given data. Implement with recursion.

        Parameters:
            data: Data to search for.

        Returns:
            Node with the given data if found, otherwise None.
        """
        if self.root is None:
            return None

        def find(node):
            if node.data == data:
                return node
            if node.left is not None and data < node.data:
                return find(node.left)
            elif node.right is not None and data > node.data:
                return find(node.right)
            return None

        return find(self.root)

    def insert(self, data) -> None:
        """
        Insert a new node into the BST. If a node with the given data already exists, 
        do nothing. Implement without/with recursion.

        Parameters:
            data: Data to store in the BST.
        """
        if self.root is None:
            self.root = Node(data)
            return
        actual_node = self.root
        while actual_node is not None:
            if actual_node.data == data:
                return
            elif actual_node.data > data:
                if actual_node.left is None:
                    actual_node.left = Node(data)
                    return
                actual_node = actual_node.left
            else:# actual_node.data <  data
                if actual_node.right is None:
                    actual_node.right = Node(data)
                    return
                actual_node = actual_node.right
                
    def _insert_into_subtree(self, data, subtree_root):
        if subtree_root is None:
            return Node(data)
        if subtree_root.data > data:
            subtree_root.left = self._insert_into_subtree(data, subtree_root.left)
        elif subtree_root.data < data:
            subtree_root.right = self._insert_into_subtree(data, subtree_root.right)
        return subtree_root   
    
    def insert_recursive(self, data) -> None:
        self.root = self._insert_into_subtree(data, self.root)

    def print(self) -> None:
        self._print_subtree(self.root)
        print()

    def _print_subtree(self, subtree_root) -> None:
        if subtree_root is None:
            return
        self._print_subtree(subtree_root.left)
        print(subtree_root, end = " ")
        self._print_subtree(subtree_root.right)


    def print_inorder(self) -> None:
        """
        Print all elements in the BST in ascending order (inorder traversal).

        Example output: 2, 8, 10
        """
        ...

    def print_structure(self) -> None:
        """
        Print the BST structure (each node on a separate line)
        with indentation reflecting tree depth.

        The traversal order (preorder, inorder, or postorder) is optional.

        Example output (for inorder traversal):

                4
            6
        7
                10
            18
                24
        """
        self._print_subtree_structure(self.root, 0)
        print()

    def _print_subtree_structure(self, subtree_root, level) -> None:
        if subtree_root is None:
            return
        self._print_subtree_structure(subtree_root.left, level + 1)
        print("  "*level, subtree_root)
        self._print_subtree_structure(subtree_root.right, level + 1)

    def delete_all(self) -> None:
        """
        Delete all nodes in the BST.

        Implement using recursion (postorder traversal) and the del statement.
        """
        self._delete_subtree(self.root)
        self.root = None

    def _delete_subtree(self, subtree_root) -> None:
        if subtree_root is None:
            return
        self._delete_subtree(subtree_root.left)
        self._delete_subtree(subtree_root.right)
        del subtree_root

    def copy(self) -> "BinarySearchTree":
        """
        Return a deep copy of the BST.

        Implement using recursion.

        Returns:
            A new BinarySearchTree containing copies of all nodes.
        """
        ...

    def delete(self, data) -> None:
        """
        Delete a node with the given data if it exists.

        Parameters:
            data: Data of the node to delete.
        """
        deleted_node, parent = self._find_node_and_parent(self.root)
        if deleted_node.left is None and deleted_node.right is None:
            self._delete_node_without_branches(deleted_node, parent)
        elif deleted_node.left is None or deleted_node.right is None:
            self._delete_node_with_one_branch(deleted_node, parent)
        else:
            self._delete_node_with_two_branches(deleted_node)

    def count(self) -> int:
        """
        Return the number of nodes in the BST.

        Implement using recursion.
        """
        if self.is_empty():
            return 0
        return self._countNodes(self.root)

    def _countNodes(self, node: Node) -> int:
        countLeft = 0
        countRight = 0
        if node.left is not None:
            countLeft = self._countNodes(node.left)
        if node.right is not None:
            countRight = self._countNodes(node.right)
        return countLeft + countRight + 1

    def depth(self) -> int:
        """
        Return the depth of the BST.

        Implement using recursion.

        Returns:
            Depth (height) of the tree.
        """
        return self._maxDepth(self.root, 0)

    def _maxDepth(self, node: Node, currDepth) -> int:
        if node is None:
            return currDepth
        leftDepth = self._maxDepth(node.left, currDepth + 1,)
        rightDepth = self._maxDepth(node.right, currDepth + 1,)
        if leftDepth > rightDepth:
            return leftDepth
        return rightDepth

    def find_min(self):
        """
        Find and return the node with the smallest data in the BST.

        Implement without recursion.

        Returns:
            Node with the smallest data, or None for an empty BST.
        """
        if self.is_empty():
            return None
        actNode = self.root
        while actNode.left is not None:
            actNode = actNode.left
        return actNode

    def serialize_to_list(self) -> list:
        """
        Preorder serialization: convert the BST to a list representation
        using preorder traversal.

        Returns:
            A list of data values stored in the BST.
        """
        return self._serializeToList(self.root, [])

    def _serializeToList(self, node: Node, lst: list) -> list:
        if node is None:
            return lst
        lst.append(node.data)
        self._serializeToList(node.left, lst)
        self._serializeToList(node.right, lst)
        return lst


    @staticmethod
    def reconstruct_from_list(input_list: list) -> "BinarySearchTree":
        """
        Deserialize a BST from the list representation produced
        by serialize_to_list().

        The internal structure of the reconstructed tree must be
        the same as the original one.

        Parameters:
            input_list: List produced by serialize_to_list().

        Returns:
            Reconstructed BinarySearchTree.
        """
        bst = BinarySearchTree()
        for node in input_list:
            bst.insert(node)
        self = bst
        return bst


    #########################################################

    def print_by_levels_recursive(self) -> None:
        """
        Print nodes level by level (level-order traversal).
        Nodes at the same depth are printed on the same line.

        Implement breadth-first traversal using recursive
        depth-first traversal.

        BONUS: Indent output to reflect tree structure.

        Example output:

               7
          3       16
        1   6      25
        """
        ...

    def print_by_levels_queue(self) -> None:
        """
        Print BST data by levels (each level on a separate line)
        using a queue.

        Implement breadth-first traversal non-recursively.

        Use the Queue class from a previous assignment.

        BONUS: Indent output to reflect tree structure.
        """
        ...
    def print_preorder_stack(self) -> None:
        """
        Print BST nodes in preorder (each node on a new line).

        Implement depth-first traversal using a stack.

        Use the Stack class from a previous assignment.

        BONUS: Indent output based on tree depth.
        """
        from collections import deque
        stack = deque()
        if self.root is not None:
            stack.append(self.root)
        while len(stack) > 0:
            actual = stack.pop()
            print(actual, end = " ")
                
            if actual.right is not None:
                stack.append(actual.right)
        
            if actual.left is not None:
                stack.append(actual.left)


    def print_postorder_stack(self) -> None:
        from collections import deque
        stack = deque()
        if self.root is not None:
            stack.append(self.root)
        while len(stack) > 0:
            actual = stack.pop()
            if isinstance(actual, Node):
                stack.append(actual.data) # here for postorder
                if actual.right is not None:
                    stack.append(actual.right)
                                        # here for inorder
                if actual.left is not None:
                    stack.append(actual.left)
                                        # here for preorder
            else:
                print(actual, end = " ")

    #########################################################

    @staticmethod
    def from_ordered_list(input_list: list) -> "BinarySearchTree":
        """
        Construct a balanced BST from a sorted list.

        Time complexity: O(n).

        Parameters:
            input_list: List of data sorted in ascending order.

        Returns:
            A balanced BinarySearchTree containing the elements.
        """
        ...


def testFind(tree):
    print("testing find")
    print("testing 3 (in):",tree.find(3))
    print("testing 56(in):",tree.find(56))
    print("testing 8(in):",tree.find(8))
    print("testing 2(not in):",tree.find(2))
    print("testing 57(not in):",tree.find(57))

def testRecursiveFind(tree):
    print("testing recursive find")
    print("testing 3 (in):",tree.recursive_find(3))
    print("testing 56(in):",tree.recursive_find(56))
    print("testing 8(in):",tree.recursive_find(8))
    print("testing 2(not in):",tree.recursive_find(2))
    print("testing 57(not in):", tree.recursive_find(57))

def testFindMin(tree):
    print("testing find min")
    findMinTree = BinarySearchTree()
    for i in range(20):
        findMinTree.insert_recursive(i)
    findMinTree.print_preorder_stack()
    print(f"smallest node (0): {findMinTree.find_min()}")
    findMinTree.insert(-1)
    findMinTree.insert(-2)
    findMinTree.insert(-13)
    findMinTree.print_preorder_stack()
    print(f"smallest node(-13){findMinTree.find_min()}")
    print("Min in passed tree:", tree.find_min())

def testCountNodes(tree):
    print("\nNum of nodes:",tree.count())
    emptyTree = BinarySearchTree()
    print("Num of nodes in empty tree:", emptyTree.count())

def testDepth(tree):
    print("\nMax depth:",tree.depth())
    emptyTree = BinarySearchTree()
    print("Depth of empty tree:", emptyTree.depth())
    emptyTree.insert(2)
    print("Depth of tree with root:", emptyTree.depth())

def testSerialization(tree):
    ser = tree.serialize_to_list()
    print("Serialized tree:", ser)
    tree1 = tree.reconstruct_from_list(ser)
    print("Reconstructed tree:")
    tree1.print_structure()
    tree1.print_preorder_stack()
    emptyTree = BinarySearchTree()
    emptyTreeSer = emptyTree.serialize_to_list()
    print("\nEmtpy serialized tree:", emptyTreeSer)
    print("Reconstructed empty tree:", tree.reconstruct_from_list(emptyTreeSer).print_preorder_stack())




if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert_recursive(12)
    tree.insert_recursive(1)
    tree.insert_recursive(20)
    tree.insert_recursive(24)
    tree.insert_recursive(13)
    tree.insert_recursive(35)
    tree.insert_recursive(17)
    tree.insert_recursive(15)
    tree.insert_recursive(30)
    tree.print_structure()
    #tree.delete_all()
    #tree.print_structure()
    tree.print_preorder_stack()
    print("\n")
    testFindMin(tree)
    testCountNodes(tree)
    testDepth(tree)
    testSerialization(tree)

