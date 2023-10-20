class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.left if self.left is not None else ''} {self.value} {self.right if self.right is not None else ''}"
        # return (
        #     f"BinaryTree({self.value}, \nleft: \t{self.left}, \tright: \t{self.right})"
        # )

    def insert(self, value):
        new_tree = BinaryTree(value)
        while self:
            if value >= self.value:
                if self.right:
                    self = self.right
                else:
                    self.right = new_tree
                    return
            if value < self.value:
                if self.left:
                    self = self.left
                else:
                    self.left = new_tree
                    return

    def dfs(self, value):  # preorder ?
        current = self
        if current:
            if current.value == value:
                return current
            left = current.left.dfs(value) if current.left else None
            right = current.right.dfs(value) if current.right else None
            if left:
                return left
            if right:
                return right
        return None

    @staticmethod
    def dfs_invert(root):
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            BinaryTree.dfs_invert(root.left)
            BinaryTree.dfs_invert(root.right)

    @staticmethod
    def findBFSmin(head):
        current = [head]
        next_nodes = []
        smallest = head
        while current:
            for node in current:
                if node.value < node.value:
                    smallest = node
                if node.left:
                    next_nodes.append(node.left)
            current = next_nodes
            next_nodes = []
        return smallest

    @staticmethod
    def dfs_remove(value, head):
        if head:
            if value < head.value:
                head.left = BinaryTree.dfs_remove(value, head.left)
            elif value > head.value:
                head.right = BinaryTree.dfs_remove(value, head.right)
            else:
                if head.left is None and head.right is None:
                    return None
                elif head.left is None:
                    return head.right
                elif head.right is None:
                    return head.right
                else:
                    inorder_successor = BinaryTree.findBFSmin(head.right)
                    head.value = inorder_successor.value
                    head.right = BinaryTree.dfs_remove(
                        inorder_successor.value, head.right
                    )
        return head

    def bfs(self, value):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.value == value:
                    return node
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            current = next
            next = []
        return False

    def bfs_invert(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
                temp = node.left
                node.left = node.right
                node.right = temp
            current = next
            next = []

    @staticmethod
    def insert_nodes(nodes: list, root):
        for node in nodes:
            root.insert(node)


if __name__ == "__main__":
    head = BinaryTree(50)
    BinaryTree.insert_nodes([75, 25, 10, 5, 7, 13, 35, 60, 80], head)
    print(head)
    BinaryTree.dfs_remove(10, head)
    # BinaryTree.dfs_invert(head)
    print(head)
    # print(head.dfs(75))
    # print(head.bfs(10))
