class BinaryTree:
    def __init__(self, root):
        self.__root = root

    def GetRoot(self):
        return self.__root

    def isRoot(self, node):
        return True if node == self.__root else False

    def size(self, node):
        if node.GetRight() != None and node.GetLeft() != None:
            return 1 + self.size(node.GetRight()) + self.size(node.GetLeft())
        elif node.GetRight() != None:
            return 1 + self.size(node.GetRight())
        elif node.GetLeft() != None:
            return 1 + self.size(node.GetLeft())
        else:
            return 1

    def printValues(self, node):
        if node.GetRight() is not None and node.GetLeft() != None:
            return str(self.printValues(node.GetRight())) +' '+  str(self.printValues(node.GetLeft())) +' '+ str(node.GetVal())
        elif node.GetRight() != None:
            return str(self.printValues(node.GetRight())) +' '+ str(node.GetVal())
        elif node.GetLeft() != None:
            return  str(self.printValues(node.GetLeft())) +' '+ str(node.GetVal())
        else:
            return str(node.GetVal())

    def sumValues(self, node):
        if node.GetRight() != None and node.GetLeft() != None:
            return node.GetVal() + self.sumValues(node.GetRight()) + self.sumValues(node.GetLeft())
        elif node.GetRight() != None:
            return node.GetVal() + self.sumValues(node.GetRight())
        elif node.GetLeft() != None:
            return node.GetVal() + self.sumValues(node.GetLeft())
        else:
            return node.GetVal()

    def numberLeaves(self, node):
        if node.GetRight() != None and node.GetLeft() != None:
            return self.numberLeaves(node.GetRight()) + self.numberLeaves(node.GetLeft())
        elif node.GetRight() != None:
            return self.numberLeaves(node.GetRight())
        elif node.GetLeft() != None:
            return self.numberLeaves(node.GetLeft())
        else:
            return 1

    def numberInternalNodes(self, node):
        if node.GetRight() != None and node.GetLeft() != None:
            return 1 + self.numberInternalNodes(node.GetRight()) + self.numberInternalNodes(node.GetLeft())
        elif node.GetRight() != None:
            return 1 + self.numberInternalNodes(node.GetRight())
        elif node.GetLeft() != None:
            return 1 + self.numberInternalNodes(node.GetLeft())
        else:
            return 0

    def height(self, node):
        if node.GetRight()!=None and node.GetLeft()!=None:
            return max(1 + self.height(node.GetRight()), 1 + self.height(node.GetLeft()))
        elif node.GetRight()!=None:
            return 1 + self.height(node.GetRight())
        elif node.GetLeft()!=None:
            return 1 + self.height(node.GetLeft())
        else:
            return 0

    def belongs(self, node, val):
        if node.GetVal() == val:
            return True
        if node.GetRight() != None :
            return self.belongs(node.GetRight(), val)
        if node.GetLeft() != None:
            return self.belongs(node.GetLeft(), val)
        else:
            return False

    def ancestors(self, node, val):
        if node.GetVal() == val:
            return ""
        if node.GetRight()!=None:
            return str(node.GetVal()) +' '+ self.ancestors(node.GetRight(), val)
        if node.GetLeft()!=None:
            return str(node.GetVal()) +' '+ self.ancestors(node.GetLeft(), val)
        else:
            return 'Pas d ancestor du noeud ayant la valeur '+str(val)

    def descendant(self, node, val):
        if node.GetVal() == val:
            a = self.printValues(node).split(" ")[:-1]
            a = " ".join(a)
            return a
        if node.GetRight() != None :
            return self.descendant(node.GetRight(), val)
        if node.GetLeft() != None:
            return self.descendant(node.GetLeft(), val)
        else:
            return 'Pas de descendant du noeud ayant la valeur '+str(val)
