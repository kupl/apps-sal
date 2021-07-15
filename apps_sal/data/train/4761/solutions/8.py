def search_k_from_end(ll, k):
    def to_list(n):
      return [n.data] if not n.next else [n.data] + to_list(n.next)
    l = list(reversed(to_list(ll.head)))
    return l[k-1] if k<=len(l) else None
