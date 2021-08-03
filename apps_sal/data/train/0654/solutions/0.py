# cook your dish here
x = int(input())
for i in range(x):
    s = list(map(int, input().split()))
    s.sort()
    print(s[1])
