import itertools
n, l = map(int, input().split())
li = [list(input().split()) for i in range(n)]
# print(li)
li.sort()
# print(li)
lis = list(itertools.chain.from_iterable(li))
print(''.join(lis))
