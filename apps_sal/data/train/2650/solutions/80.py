import itertools
n, l = map(int, input().split())
li = [list(input().split()) for i in range(n)]
li.sort()
lis = list(itertools.chain.from_iterable(li))
print(''.join(lis))
