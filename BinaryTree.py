class BinaryTree:
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # ------- Insert Methods -------
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        # Base case: empty spot
        if current_node is None:
            return self.Node(value)

        # Recursive step: go left or right
        if value < current_node.value:
            current_node.left = self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._insert_recursive(current_node.right, value)
        # else: value already exists (no duplicates)

        return current_node

    # ------- Search Method -------
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        # Base case 1: not found
        if current_node is None:
            return False

        # Base case 2: found
        if value == current_node.value:
            return True

        # Recursive step
        if value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    # ------- Traversal Methods -------
    # In-Order (Left -> Root -> Right)
    def in_order(self):
        print("In-Order:    ", end="")
        self._in_order_recursive(self.root)
        print()

    def _in_order_recursive(self, node):
        if node is not None:
            self._in_order_recursive(node.left)
            print(node.value, end=" ")
            self._in_order_recursive(node.right)

    # Pre-Order (Root -> Left -> Right)
    def pre_order(self):
        print("Pre-Order:   ", end="")
        self._pre_order_recursive(self.root)
        print()

    def _pre_order_recursive(self, node):
        if node is not None:
            print(node.value, end=" ")
            self._pre_order_recursive(node.left)
            self._pre_order_recursive(node.right)

    # Post-Order (Left -> Right -> Root)
    def post_order(self):
        print("Post-Order:  ", end="")
        self._post_order_recursive(self.root)
        print()

    def _post_order_recursive(self, node):
        if node is not None:
            self._post_order_recursive(node.left)
            self._post_order_recursive(node.right)
            print(node.value, end=" ")

