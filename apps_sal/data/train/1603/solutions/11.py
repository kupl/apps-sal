from itertools import groupby
web_addresses_number = int(input())
prephix = "http://"
def split_address(address):
    host = ""
    path = ""
    address = address[7:]
    i = 0
    while i < len(address) and address[i] != '/':
        host += address[i]
        i += 1
    while i < len(address):
        path += address[i]
        i += 1
    return (host, path)
hosts = {}
for i in range(web_addresses_number):
    host, path = split_address(input())
    if host in hosts:
        hosts[host].add(path)
    else:
        hosts[host] = {path}
groups = []
hosts = {host:"+".join(sorted(hosts[host])) for host in hosts}
groping = groupby(sorted(hosts, key = lambda host: hosts[host]), key = lambda host: hosts[host])
for key, group in groping:
    g = list(group)
    if len(g) > 1:
        groups.append(g)
print(len(groups))
[print(" ".join(map(lambda host: prephix + host, group))) for group in groups]

