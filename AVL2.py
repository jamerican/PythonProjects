class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.bf = 0

class AVL_TREE:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
            return True
        else:
            return self.insert_helper(self.root, key)

    def insert_helper(self, root, key):
        if root == None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_helper(root.left, key)
            self.update(root)
            return True
        else:
            root.right = self.inset_helper(root.right, key)
            self.update(root)
            return True
        return False


    #BR Update Methods
    def update(self, root):
        root.bf = height(root.right) - height(root.left)

    def height

    #Balance Methods

