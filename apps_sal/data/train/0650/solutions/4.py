from sys import stdin, stdout
input = stdin.readline
print2 = stdout.write
def get_list(): return tuple(map(int, stdin.readline().split()))


for _ in range(int(input())):
    n, k = map(int, stdin.readline().split())
    event = sorted([get_list() for _ in range(n)])
    occup = {}
    count = 0
    for e in event:
        if not occup.get(e[2]) or e[0] >= occup[e[2]][1]:
            occup[e[2]] = e
            count += 1
        elif e[1] < occup[e[2]][1]:
            occup[e[2]] = e
    print(count)
