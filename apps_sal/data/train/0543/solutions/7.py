# cook your dish here
for _ in range(int(input())):
    rt = int(input())
    tr = list(map(int, input().split()))
    rd = int(input())
    dr = list(map(int, input().split()))
    st = int(input())
    ts = list(map(int, input().split()))
    sd = int(input())
    ds = list(map(int, input().split()))
    l = []
    for i in ts:
        if i in tr:
            l.append('y')
        else:
            l.append('no')
    for i in ds:
        if i in dr:
            l.append('y')
        else:
            l.append('no')
    if "no" in l:
        print("no")
    else:
        print("yes")
