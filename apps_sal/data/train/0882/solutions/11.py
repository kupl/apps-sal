# cook your dish here
for _ in range(int(input())):
    a, b = input(), input()
    l = 0
    for x in set(a) & set(b):
        l += min(a.count(x), b.count(x))
    print(l)
