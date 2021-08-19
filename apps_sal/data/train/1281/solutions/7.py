# cook your dish here
t = int(input())
x = [1, 2, 3, 4, 5, 6, 7]
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    l = s[::-1]
    r = set(s)
    if(s == l and list(r) == x):
        print("yes")
    else:
        print("no")
