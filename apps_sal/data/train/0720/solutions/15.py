dic = {}
for i in range(1, 316):
    dic[i - 1] = (i * (i + 1), i)

t = int(input())
for _ in range(t):
    arr = list(map(int, input().rstrip()))
    n = len(arr)
    for i in range(1, n):
        arr[i] += arr[i - 1]
    arr.append(0)
    ans = 0
    for length, cnt1 in dic.values():
        i = 0
        while(i + length - 1 < n):
            real_cnt1 = arr[i + length - 1] - arr[i - 1]
            if(real_cnt1 == cnt1):
                ans += 1
                i += 1
            else:
                i += abs(cnt1 - real_cnt1)

    print(ans)
