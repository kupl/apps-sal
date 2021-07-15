def merge_arrays(first, second): 
    ans = first + second
    ans.sort()
    unique = []
    for i in ans:
        if i not in unique:
            unique.append(i)
    return unique
