# cook your dish here
for _ in range(int(input())):
    num, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if(k <= num // 2):
        arr.sort()
        ans = sum(arr[k:]) - sum(arr[:k])
        print(abs(ans))
    else:
        arr.sort()
        ans = sum(arr[num - k:]) - sum(arr[:num - k])
        print(ans)
