A, B, C = list(map(int, input().split()))
X = int(input())
print(sum(B < x < C for x in map(int, input().split())))
