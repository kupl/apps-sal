# cook your dish here
for i in range(int(input())):
    a, b = map(int, input().split())
    a = set(str(a))
    print(len(a)**3)
