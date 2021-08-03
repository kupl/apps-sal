# your code goes here
t = eval(input())
for i in range(0, t):
    a, b = list(map(int, input().split()))
    if(b == 1):
        print(0)
    else:
        ans = b * ((b - 1)**(a - 1))
        ans = ans % 1000000007
        print(ans)
