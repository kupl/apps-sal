# cook your dish here
# cook your dish here
for i in range(int(input())):
    N = int(input())
    Arr = list(map(int, input().split()))
    ans = 0
    for i in Arr:
        if i % 6 == 0:
            ans += 6
        else:
            ans += i - int(i / 6) * 6
    print(ans)
