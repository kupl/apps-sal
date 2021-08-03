# cook your dish here
# cook your dish here
# cook your dish here
T = int(input())

for i in range(T):
    a, b, c = map(int, input().split())

    rem = c % a
    k = c - rem + b

    while(k > c):
        k = k - a

    print(k)
