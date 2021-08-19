# cook your dish here

for _ in range(int(input())):
    l = list(map(int, input().split()))
    a = list(map(int, input().split()))
    s = sum(a)
    d = s // l[1]

    if(d > l[2]):
        print(l[2])
    else:
        print(d)
