def search_k_from_end(linked_list, k):
    l = [linked_list.head.data]
    n = linked_list.head.next
    while n:
        l.append(n.data)
        n = n.next
    return None if k > len(l) else l[-k]
