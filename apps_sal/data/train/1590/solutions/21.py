n = int(input())
for i in range(n):
    li = [int(i) for i in input().split()]
    print('Yes' if sum(li) - max(li) >= max(li) else 'No')
