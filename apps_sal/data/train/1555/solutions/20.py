# cook your dish here
T = int(input())
while T > 0:
    N = int(input())
    T = T - 1
    A = (N - 1)**2 + N**3
    print(A % 1000000007)
