def men_from_boys(arr):
    even = []
    odd = []
    for a in arr:
        if a % 2 == 0:
            if a not in even:
                even.append(a)
        elif a not in odd:
            odd.append(a)
    print(even)
    print(odd)
    odd.sort(reverse=True)
    even.sort()
    for o in odd:
        even.append(o)
    return even
