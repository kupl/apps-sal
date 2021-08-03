n = int(input())
a = list(map(int, input().split()))
x = 0
for i in a:
    x ^= i
print(* list(map(lambda y: x ^ y, a)))
