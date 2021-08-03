# cook your dish here
T = int(input())
for i in range(T):
    m, n = list(map(int, input().split()))
    if m < n:
        print("<")
    elif m > n:
        print(">")
    else:
        print("=")
