import sys
from urllib.parse import urlparse
import itertools as itt


def main():
    n = int(sys.stdin.readline().strip())
    links = [sys.stdin.readline().strip() for i in range(n)]
    host_queries = {}
    for link in links:
        p = urlparse(link)
        host = 'http://' + p.netloc
        query = p.path
        if not host in host_queries:
            host_queries[host] = set()
        host_queries[host].add(query)
    hosts = list(host_queries.keys())
    hosts = list(sorted(hosts, key=lambda h: '-'.join(sorted(host_queries[h]))))
    groups = []
    for (key, group) in itt.groupby(hosts, key=lambda h: '-'.join(sorted(host_queries[h]))):
        g = list(group)
        if len(g) < 2:
            continue
        groups.append(g)
    print(len(groups))
    for g in groups:
        print(' '.join(g))


def __starting_point():
    main()


__starting_point()
