testcases = int(input())
for x in range(testcases):
    n = int(input())
    li = [(x + 1) ** 3 for x in range(n)]
    print(sum(li) + sum(li[:-1]))
