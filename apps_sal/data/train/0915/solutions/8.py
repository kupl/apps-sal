# cook your dish here
t = int(input())
l = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a1 = set(a)
    print(len(a1))
