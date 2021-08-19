# cook your dish here
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    # n=int(input())
    print(max(a, b), a + b)
