from Node import *
from BinaryTree import*

N21 = Node(21, None, None)
N18 = Node(18, None, None)
N3 = Node(3, None, None)
N6 = Node(6, None, None)
N4 = Node(4, N3, None)
N19 = Node(19, N18, N21)
N17 = Node(17, None, N19)
N5 = Node(5, N4, N6)
N12 = Node(12, N5, N17)
tree = BinaryTree(N12)

print(tree.size(N12))
print(tree.printValues(N12))
print(tree.sumValues(N12))
print(tree.numberLeaves(N12))
print(tree.numberInternalNodes(N12))
print(tree.height(N12))
print(tree.belongs(N12, 19))
print(tree.ancestors(N12, 21))
print(tree.descendant(N12, 19))
