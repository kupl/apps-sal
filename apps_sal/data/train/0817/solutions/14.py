# cook your dish here
test = int(input())

for i in range(test):
    n = int(input())
    val = list(map(int, input().split()))

    x = 0
    if(len(val) == n):
        for i in val:
            x ^= i
        print(x)
