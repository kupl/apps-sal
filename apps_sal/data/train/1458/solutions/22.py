# cook your dish here
for t in range(int(input())):
    N = int(input())
    sum = 0
    for i in range(1, N + 1, 2):
        sum += (N - i + 1) ** 2
    print(sum)
