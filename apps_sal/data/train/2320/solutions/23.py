def ii(): return int(input())
def mi(): return list(map(int, input().split()))
def li(): return list(mi())
def si(): return input()
def msi(): return list(map(int, stdin.readline().split()))
def lsi(): return list(msi())


m = int(input())

a = list(map(int, input().split()))
b = list(zip(list(map(int, input().split())), list(range(m))))

a.sort(reverse=True)
b.sort()

c = list(zip((t[1] for t in b), a))
c.sort()

print(*(t[1] for t in c))
