t = int(input())
while(t):
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    if(len(set(a)) == 1):
        print(1)
        print("1 "*n)
    elif(n % 2 == 0):
        print(2)
        print("1 2 " * (n // 2))
    else:
        ans = [1]
        en = 1
        colour = 2
        for i in range(1, n):
            if(en and a[i] == a[i-1]):
                colour = 3 - colour
                en = 0
            ans.append(colour)
            colour = 3 - colour
        if(a[-1] != a[0] and ans[-1] == 1):
            ans[-1] = 3
        print(max(ans))
        print(*ans)
