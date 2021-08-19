# cook your dish here
def f(x):
    sumi = 0
    for i in li:
        sumi += (abs((x - i)))**k
    return sumi


def binary_search(l, r):
    mid = (l + r) // 2
    if(f(mid) < f(mid - 1)):
        if(f(mid) <= f(mid + 1)):
            return mid
        return binary_search(mid + 1, r)
    return binary_search(l, mid - 1)


l = input().split()
n = int(l[0])
k = int(l[1])
l = input().split()
li = [int(i) for i in l]
print(binary_search(0, 5 * (10**4) + 5))
