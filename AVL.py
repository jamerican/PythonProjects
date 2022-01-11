class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.bf = 0

class AVL_TREE:
    def __init__(self):
        self.root = None

    #BST METHODS
    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            return self.insert_helper(self.root, key)

    def insert_helper(self, root, key):
        if root.left == None and root.right == None:
            if key < root.key:
                root.left = Node(key)
                #update()
                #balance()
                return True
            else:
                root.right = Node(key)
                #update()
                #balance()
                return True
        else:
            if key < root.key:
                if root.left == None:
                    root.left = Node(key)
                    #update
                    #balance
                else:
                    return self.insert_helper(root.left, key)
            elif key > root.key:
                if root.right == None:
                    root.right = Node(key)
                    #update
                    #balance
                else:
                    return self.insert_helper(root.right, key)
            else:
                return False

    def delete(self, key):
        pass

    def delete_helper(self, root, key):
        pass

    #Update Method



    #Balance Methods

    #This is a test update


