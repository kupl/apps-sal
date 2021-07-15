# pass in the linked list
# to access the head of the linked list
# linked_list.head
def search_k_from_end(l, k):
    #todo
    m, n = l.head, l.head
    while k:
        if not n:
            return None
        n = n.__next__
        k -= 1
    while n:
        m = m.__next__
        n = n.__next__
    return m and m.data
        

