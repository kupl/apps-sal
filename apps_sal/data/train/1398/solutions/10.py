T = int(input())
ans = []
for _ in range(T):
    A = input()
    ans.append(len(set(list(A))))
for i in ans:
    print(i)
