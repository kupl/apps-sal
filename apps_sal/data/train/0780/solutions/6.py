t = (int)(eval(input()))
while(t > 0):
    t = (int)(t - 1)
    n, m = list(map(int, input().split()))
    x = (int)(n % m)
    if(x % 2 == 0):
        print("EVEN")
    else:
        print("ODD")
