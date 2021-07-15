""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if not head:
        return Node(data)
    elif head.data>data:
        res=Node(data)
        res.next=head
        return res
    else:
        temp=head
        while head.next and head.next.data<data:
            head=head.next
        res=Node(data)
        res.next=head.next
        head.next=res
        return temp
        return temp
