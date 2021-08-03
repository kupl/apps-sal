# cook your dish here
class node:
    def __init__(self, a, b=0, c=0):
        self.val = a
        self.a = b
        self.b = c


arr = []


def finder(node, val):
    if(arr[node].val == 0):
        return val
    else:
        a = finder(arr[node].a, val)
        b = finder(arr[node].b, val)
        if(arr[node].val == 1):
            return a + b - a * b
        else:
            return a * b


t = int(input())
while(t > 0):
    x = input()
    n = int(input())
    arr.append(node(0))
    for i in range(0, n):
        vals = input().split()
        sz = len(vals)
        for i in range(0, sz):
            vals[i] = int(vals[i])
        if(vals[0] == 0):
            next = node(0)
            arr.append(next)
        else:
            next = node(vals[0], vals[1], vals[2])
            arr.append(next)
    lower = 0.0
    higher = 1.0
    eps = 1e-9
    while((higher - lower) > eps):
        mid = (higher + lower) / 2.0
        if(finder(n, mid) > 0.5):
            higher = mid
        else:
            lower = mid
    print("%.5f" % (higher))
    arr = []
    # print(higher)
    t -= 1
