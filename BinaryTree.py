
class BinaryTree:
    def __init__(self, root):
        self.__root = root

    def GetRoot(self):
        return self.__root

"""
    def isRoot(self, node):
        return True if node == self.__root else False

    def size(self, node):
        if node.GetRight() == None and node.GetLeft() == None:
            return
        else:
            return 1 + self.size(se)
"""
