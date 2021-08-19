# cook your dish here
tc = int(input())
for t in range(tc):
    n = int(input())
    st = input()
    c = 0
    for i in range(1, n):
        if st[i] == st[i - 1]:
            i += 1
            c += 1
    print(c)
