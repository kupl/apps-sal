for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    j = 0
    count = 0
    for i in range(len(a)):
        if a[i] == b[j]:
            count += 1
            j += 1
            if j == m:
                break
    if count == m:
        print('Yes')
    else:
        print('No')
