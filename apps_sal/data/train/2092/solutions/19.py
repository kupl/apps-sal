n = int(input())
s = input()
a = [input() for i in range(n)]
f = sum((s + '->' in i for i in a))
t = sum(('->' + s in i for i in a))
if f == t:
    print('home')
else:
    print('contest')
