N = int(input())
A = list([x for x in map(int, input().split()) if x < 0])
X = int(input())
coins = 0
if len(A) <= X:
    coins += abs(sum(A))
else:
    A.sort(reverse=True)
    coins = abs(sum(A[len(A) - X:]))
print(coins)
