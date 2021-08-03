from sys import stdin

# Input data
#stdin = open("input", "r")


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    for i in range(int(stdin.readline())):
        a, b = list(map(int, stdin.readline().split()))
        print(sum(arr[a - 1:b]))
