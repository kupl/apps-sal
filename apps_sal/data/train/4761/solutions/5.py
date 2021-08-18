def search_k_from_end(linked_list, k):
    head = linked_list.head
    count = 0
    while head != None:
        count += 1
        head = head.__next__
    head = linked_list.head
    if k > count:
        return None
    while count - k > 0:
        count -= 1
        head = head.__next__
    return head.data
