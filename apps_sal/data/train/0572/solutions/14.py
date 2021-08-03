# cook your dish here
x = int(input())
for i in range(x):
    (a, b, c) = map(int, input().split())
    if abs(a - b) == c or abs(a - b) < c:
        print("0")
    elif abs(a - b) > c:
        print(abs(a - b) - c)
