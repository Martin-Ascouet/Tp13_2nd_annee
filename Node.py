class Node:
    def __init__(self, val, left = None, right = None):
        self.__val = val
        self.__right = right
        self.__left = left

    def GetVal(self):
        return self.__val

    def GetRight(self):
        return self.__right

    def GetLeft(self):
        return self.__left

    def SetRight(self, right):
        self.__right = right

    def SetLeft(self, left):
        self.__left = left


