import sys

d = dict()
b='/'
for line in sys.stdin:
	line=line[:-1].split(b)

	host,coso=b.join(line[:3]), b.join(line[3:])

	if len(line)>3: coso='/'+coso
	if len(line)>1:

		if host in d: d[host].append("I"+coso)
		else: d[host]=["I"+coso]

for host in d:
	b = ','
	d[host]=sorted(set(d[host]))
	d[host]=b.join(d[host])

d2=dict()

for host in d:
	if d[host] in d2: d2[d[host]].append(host)
	else:	d2[d[host]]=[host]

print(sum([len(d2[x])>1 for x in d2]))

for x in d2:
	ans = ""
	if len(d2[x])>1:
		for i in d2[x]: ans+=i+' '
		print (ans)

