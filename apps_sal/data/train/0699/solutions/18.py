# cook your dish here
for _ in range(int(input())):
    n, k, d = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    t = sum(A)
    if(t < k):
        print(0)
    else:
        res = t // k
        print(min(res, d))
