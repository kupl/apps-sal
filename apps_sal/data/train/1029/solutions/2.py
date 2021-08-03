# cook your dish here
def work(a):
    chef = []
    asst = []
    c = True
    t = False
    for i in range(1, len(a)):
        if a[i] != 1:
            if c:
                chef.append(i)
                c = False
                t = True
            else:
                asst.append(i)
                t = False
                c = True
    return chef, asst


t = int(input())
while t:
    n, m = [int(k) for k in input().split()]
    a = [0] * (n + 1)
    finished = [int(k) for k in input().split()]
    for i in finished:
        a[i] = 1
    chef, asst = work(a)
    for i in chef:
        print(i, end=' ')
    print()
    for i in asst:
        print(i, end=' ')
    print()
    t -= 1
