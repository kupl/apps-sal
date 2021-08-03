for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    s = sum(a) / n
    m = 0
    store = 0
    buy = 0
    if int(s) != s:
        s = int(s) + 1
    for i in a:
        if(i < s):
            buy += s - i
        elif(i > s):
            store += i - s
            m += i - s
    if(store < buy):
        m += buy - store
    print(m)
