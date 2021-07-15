remove_smallest = lambda m, n=[]: n.clear() or n.extend(m) or ((n.remove(min(n)) or n) if n else n)
