for _ in range(int(input())):
    lst = []
    for nn in range(int(input())):
        stg = input()
        chck = list(set(stg))
        if chck == ['a'] or chck == ['b']:
            lst.append(0)
            continue
        else:
            lst.append(min(stg.count('a'), stg.count('b')))
    print(min(lst))
