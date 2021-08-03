# pass in the linked list
# to access the head of the linked list
# linked_list.head
def search_k_from_end(linked_list, k):
    head = linked_list.head
    vals = []
    while head:
        vals.append(head.data)
        head = head.__next__
    return vals[-k] if k <= len(vals) else None
