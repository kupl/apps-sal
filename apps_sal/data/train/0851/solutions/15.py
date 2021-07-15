def my(n,k):
    num = 2*(1+(k-1)*n)
    den = k
    return num/den

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(my(n, k))
