from collections import Counter, defaultdict

for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    coun = Counter(arr)
    check = True

    for j in coun:
        if coun[j] > n // 2:
            print("No")
            check = False
            break

    if check == True:
        print("Yes")
        narr = sorted(arr)
        dic = defaultdict()
        j = 0
        for j in range(len(narr)):
            if narr[j] not in dic:
                dic[narr[j]] = j
        ans = [0] * n
        for j in range(len(arr)):
            ans[j] = narr[(dic[arr[j]] + n // 2) % n]
            if coun[arr[j]] != 1:
                dic[arr[j]] += 1
        print(*ans)
