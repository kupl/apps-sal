for __ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ans = []
    kek = set()
    for elem in ar:
        if elem not in kek:
            kek.add(elem)
            ans.append(elem)
    print(*ans)
