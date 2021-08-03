class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(list):
    if list == None:
        return 'None'
    else:
        return str(list.data) + ' -> ' + stringify(list.next)
