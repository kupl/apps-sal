def search_k_from_end(linked_list, k):
    a = b = linked_list.head

    for __ in xrange(k - 1):
        b = b.next
        if not b:
            return None

    while b.next:
        a, b = a.next, b.next

    return a.data
