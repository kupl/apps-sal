import re

url_parser = re.compile(r"^http://([^/]+)(.*)")
while True:
    try:
        k = int(input())
    except EOFError:
        break

    d = {}
    for _ in range(k):
        hostname, path = url_parser.findall(input())[0]
        if hostname in d:
            d[hostname].add(path)
        else:
            d[hostname] = set((path,))

    d_reverse = {}
    for hostname, pathset in d.items():
        thumb = "_".join(sorted(pathset))
        if thumb in d_reverse:
            d_reverse[thumb].append(hostname)
        else:
            d_reverse[thumb] = [hostname]

    ans = [line for line in d_reverse.values() if len(line) > 1]
    print(len(ans))
    for line in ans:
        print(" ".join(map(lambda x: "http://" + x, line)))
