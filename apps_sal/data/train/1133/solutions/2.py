# cook your dish here
def factors(n):
    res = []
    for i in range(n // 2, 0, -1):
        if (n % i == 0):
            res.append(i)
    return res


def wires(w):
    w.sort()
    a = w[0]
    cost = 0
    for num in w:
        if (num % a != 0):
            fact = factors(a)
            break
        cost = cost + (num // a)
    else:
        print(a, cost)
        return None
    for char in fact:
        cost = 0
        for num in w:
            if (num % char != 0):
                break
            cost = cost + (num // char)
        else:
            print(char, cost)
            return None


t = int(input())
for _ in range(t):
    n = int(input())
    w = [int(x) for x in input().split()]
    wires(w)
