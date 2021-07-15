from sys import stdin, stdout
n = int(stdin.readline())
#l = list(map(int, stdin.readline().split()))
#l = [int(stdin.readline()) for _ in range(n)]
#a, b = map(int, stdin.readline().split())
for _ in range(n):
    n1 = int(stdin.readline())
    abd = (n1*(n1-1))//2
    print(abd)
