
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self, root):
        self.root = Node(root)

    def insert(self):
        # consider the balancing act
        # think about powers of 2
        pass

    def delete(self):
        # consider the balancing act
        pass

    def height_balance(self):
        pass


def in_order_traversal(node: Node):
    # left, root, right
    # most used

    if node:
        in_order_traversal(node.left)
        print(node.value, end=" -> ")
        in_order_traversal(node.right)

def pre_order_traversal(node: Node):
    # root, left, right
    # most used
    if node:
        print(node.value, end=" -> ")
        in_order_traversal(node.left)
        in_order_traversal(node.right)

def post_order_traversal(node: Node):
    # left, right, root
    if node:
        in_order_traversal(node.left)
        in_order_traversal(node.right)
        print(node.value, end=" -> ")


# Main driver code
if __name__ == "__main__":
    some_b_tree = BinaryTree(10)
    some_b_tree.root.left = Node(20)
    some_b_tree.root.right = Node(30)
    some_b_tree.root.right.right = Node(60)
    some_b_tree.root.left.left = Node(40)
    some_b_tree.root.left.left.left = Node(50)
    print("In-order traversal results: ", end="")
    in_order_traversal(some_b_tree.root)
    print()
    print("Preorder traversal results: ", end ="")
    pre_order_traversal(some_b_tree.root)
    print()
    print("Post-order traversal results: ", end ="")
    post_order_traversal(some_b_tree.root)
    print()

"""r
In-order traversal results: 50 -> 40 -> 20 -> 10 -> 30 -> 60 -> 
Preorder traversal results: 10 -> 50 -> 40 -> 20 -> 30 -> 60 -> 
Post-order traversal results: 50 -> 40 -> 20 -> 30 -> 60 -> 10 -> 
"""