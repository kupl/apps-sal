n = int(input())
hosts = dict()
for i in range(n):
    inp = input()
    pos = inp.find("/", 7)
    if pos == -1: pos = len(inp)
    hostName = inp[:pos]
    path = inp[pos:]
    if hostName not in hosts:
        hosts[hostName] = set()
    hosts[hostName].add(path)

groups = dict()
for name in hosts.keys():
    paths = tuple(sorted(hosts[name]))
    if paths not in groups:
        groups[paths] = []
    groups[paths].append(name)

ans = []
for group in groups.values():
    if len(group) > 1:
        ans.append(group)

print(len(ans))
for group in ans:
    print(" ".join(group))
