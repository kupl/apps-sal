def args_count(*t, **a1):
    print(t)
    print(a1)
    if a1:
        return len(t) + len(a1)
    else:
        return len(t)
