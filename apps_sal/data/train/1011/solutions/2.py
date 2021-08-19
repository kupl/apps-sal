# cook your dish here
t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    a = input()
    c = 0
    b = 0
    for i in a:
        if i.isupper():
            c += 1
        else:
            b += 1
    if c <= k and b > k:
        print("chef")
    elif c > k and b <= k:
        print("brother")
    elif c <= k and b <= k:
        print('both')
    elif c > k and b > k:
        print("none")
