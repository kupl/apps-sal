# cook your dish here
for i in range(int(input())):
    a = list(map(int, input().split()))
    x = input()
    tot = 0
    for i in range(97, 123):
        if chr(i) not in x:
            tot += a[i - 97]
    print(tot)
