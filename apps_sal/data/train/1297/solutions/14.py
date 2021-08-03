# cook your dish here
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if x == y:
        print("=")
    else:
        a = ">" if x > y else "<"
        print(a)
