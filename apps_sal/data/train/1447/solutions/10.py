for _ in range(int(input())):
    n = int(input())
    inp = list(map(int, input().split()))
    ing = [inp[0]]
    count = []
    last = inp[0]
    ans = "YES"
    cnt = 1
    for i in range(1, n):
        if last == inp[i]:
            cnt += 1
        else:
            if cnt not in count and (inp[i] not in ing):
                count.append(cnt)
                cnt = 1
                last = inp[i]
                ing.append(last)
            else:
                ans = "NO"
                break

    if cnt in count:
        ans = "NO"
    print(ans)
