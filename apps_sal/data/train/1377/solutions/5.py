# cook your dish here
t = int(input())
for z in range(t):
    th, tl, nh, nl = list(map(int, input().split()))
    diff = (th + tl - nh - nl) / 2
    if(diff >= 0):
        print(str(1.0 * diff) + " DEGREE(S) ABOVE NORMAL")
    else:
        diff = -1.0 * diff
        print(str(1.0 * diff) + " DEGREE(S) BELOW NORMAL")
