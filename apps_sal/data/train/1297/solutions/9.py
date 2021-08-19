# cook your dish here
for t in range(int(input())):
    x, y = map(int, input().split())
    if x == y:
        print("=")
    else:
        a = ">" if x > y else "<"
        print(a)
