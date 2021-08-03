for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    isContinuing = set()
    ans = 0
    for i in l:
        lengthOfSet = len(isContinuing)
        isContinuing.add(i)
        if(lengthOfSet == len(isContinuing)):
            ans += 2
            isContinuing.clear()
    print(n - ans)
