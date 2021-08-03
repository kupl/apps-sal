def sort_string(s, ordering):
    return "".join(sorted([i for i in s if i in ordering], key=lambda x: ordering.index(x))) + "".join(sorted([j for j in s if j not in ordering], key=lambda x: s.index(s)))
