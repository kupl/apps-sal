n = eval(input())
reports = set(map(int, input().split()))
print(' '.join(str(i) for i in range(n + 1) if i not in reports))
