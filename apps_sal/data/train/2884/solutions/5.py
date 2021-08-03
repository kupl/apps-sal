class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def getValue(self):
    return self.data


def getNext(self):
    return self.__next__


def stringify(node):
    if node == None:
        return 'None'
    return str(getValue(node)) + ' -> ' + stringify(getNext(node))
