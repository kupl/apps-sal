n = eval(input())
s = input()
numbers = list(map(int, s.split()))
s1 = set(range(1, n + 1))
s2 = set(numbers) - set([0])
for i in sorted(list(s1 - s2)):
    print(i, end=' ')
