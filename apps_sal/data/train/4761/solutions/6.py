def search_k_from_end(l, k):
    head, li = l.head, []
    while head:
        li.append(head.data)
        head = head.next
    return li[-k] if k <= len(li) else None
