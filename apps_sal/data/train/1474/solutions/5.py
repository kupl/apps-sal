tc = int(input())
for i in range(tc):
    m = -1
    n = int(input())
    p = list(map(str, input().split()))
    q = input()
    no = 0
    for j in p:
        if q in j:
            l = j.count(q)
            if m < l:
                m = l
                no = j
    print(no)
