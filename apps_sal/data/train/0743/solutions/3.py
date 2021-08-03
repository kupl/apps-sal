# cook your dish here
def hii(a, b):
    if b == 1:
        print('NO')
    elif (a // b) % b != 0:
        print('YES')
    else:
        print('NO')


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    hii(n, k)
