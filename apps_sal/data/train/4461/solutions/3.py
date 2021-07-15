def boxes_packing(l,w,h):
    return all(len(i)==len(set(i))and list(i)==sorted(i)for i in list(zip(*sorted(sorted(i)for i in list(zip(l,w,h))))))
