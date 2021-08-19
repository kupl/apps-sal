# cook your dish here
def program():
    n, q = map(int, input().split())
    l = list(map(int, input().split()))

    for i in range(q):
        a, b = map(int, input().split())
        print(sum(l[a - 1:b]))


t = int(input())
for i in range(t):
    program()
