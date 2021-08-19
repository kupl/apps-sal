# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if sum(A) % N == 0:
        print("Yes")
    else:
        print("No")
