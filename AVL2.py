class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.bf = 0

class AVL_TREE:
    def __init__(self):
        self.root = None

    #Insert Methods
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return True
        else:
            return self.insert_helper(self.root, key)

    def insert_helper(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_helper(root.left, key)
            #self.update(root)
            return True
        else:
            root.right = self.inset_helper(root.right, key)
            #self.update(root)
            return True
        return False

    #Delete Method
    def delete(self, key):
        pass

    def delete_helper(self, root, key):
        pass


    #BR Update Methods
    def update(self, root):
        root.bf = self.height(root.right) - self.height(root.left)
        if -1 >= root.bf <= 1:
            return
        else:
            self.balance(root)

    #Balance Method
    def balance(self, root):
        if root.bf == -2:
            if root.left.bf == -1:
                self.LeftLeftRotate(root)
            else:
                self.LeftRightRotate(root)
        elif root.bf == 2:
            if root.right == 1:
                self.RightRightRotate(root)
            else:
                self.RightLeftRotate(root)

    #Rotation Methods
    def LeftLeftRotate(self, root):
        pass
    def LeftrightRotate(self, root):
        pass
    def RightRightRotate(self, root):
        pass
    def RightLeftRotate(self, root):
        pass

    #Helper Methods
    def parent(self, root):
        if root.key == self.root.key:
            return None
        else:
            return self.parent_helper(root.key, self.root)

    def parent_helper(self, key, root):
        if key < root.key:
            if root.left.key == key:
                print(root.key)
                return root
            else:
                return self.parent(key, root.left)
        elif key > root.key:
            if root.right.key == key:
                print(root.key)
                return root
            else:
                return self.parent(key, root.right)

    def height(self, root):
        if root.left is None and root.right is None:
            return 0
        else:
            left_tree = 1 + self.height(root.left)
            right_tree = 1 + self.height(root.right)
            return max(left_tree, right_tree)

