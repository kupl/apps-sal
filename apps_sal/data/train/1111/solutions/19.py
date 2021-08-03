# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    odd = 0
    even = 0
    for j in a:
        if(j % 2 == 0):
            even += 1
        else:
            odd += 1
    print(odd * even)
