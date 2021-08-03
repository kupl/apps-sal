t = int(input())
for i in range(t):
    a = input().split()
    print(int(repr(int(a[0][::-1]) + int(a[1][::-1]))[::-1]))
