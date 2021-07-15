n = int(input())

domains = {}
for _ in range(n):
    request = input()[7:]

    domain, sep, path = request.partition('/')

    if domain in domains:
        domains[domain].add(sep + path)
    else:
        domains[domain] = {sep + path}

path_hashes = []
for domain, paths in list(domains.items()):
    path_hashes.append(('|'.join(sorted(paths)), domain))

sorted_hashes = sorted(path_hashes, key=lambda x: x[0])

previous_hash = None
previous_domains = []
groups = []

for path_hash, domain in sorted_hashes:
    if previous_hash == path_hash:
        previous_domains.append(domain)
    else:
        previous_hash = path_hash
        if len(previous_domains) > 1:
            groups.append(previous_domains)
        previous_domains = [domain]

if len(previous_domains) > 1:
    groups.append(previous_domains)

print(len(groups))
print('\n'.join([' '.join(['http://' + y for y in x]) for x in groups]))

