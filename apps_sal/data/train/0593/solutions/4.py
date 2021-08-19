# cook your dish here
for i in range(int(input())):
    a = list(map(int, input().split()))
    x = input()
    t = 0
    for i in range(97, 123):
        if chr(i) not in x:
            t += a[i - 97]
    print(t)
