3

import functools
import itertools
import operator


def split(address):
	address = address[7:]
	p = address.find('/')
	if p == -1:
		return address, ''

	return address[:p], address[p:]


def set_key(addr1, addr2):
	pages1, pages2 = addr1[1], addr2[1]
	l1 = len(pages1)
	l2 = len(pages2)
	if l1 != l2:
		return l2 - l1

	for page1, page2 in zip(pages1, pages2):
		if page1 < page2: return -1
		if page1 > page2: return 1

	return 0;


def solve(addresses):
	addresses = list(map(split, addresses))

	m = dict()
	for domain, page in addresses:
		if domain in m:
			m[domain].add(page)
		else:
			m[domain] = {page}

	l = [(domain, sorted(pages)) for domain, pages in list(m.items())]

	l.sort(key=functools.cmp_to_key(set_key))

	groups = []

	gb = itertools.groupby(l, key=operator.itemgetter(1))
	for key, group in gb:
		group_domains = ['http://'+d for d,ps in group]
		if(len(group_domains) > 1):
			groups.append(group_domains)

	# print(groups)
	return groups


def main():
	n = int(input())
	addresses = [None]*n

	for i in range(n):
		addresses[i] = input()

	groups = solve(addresses)

	print(len(groups))
	for group in groups:
		print(' '.join(group))


def test():
	# addresses = """
	# 	http://abacaba.ru/test
	# 	http://abacaba.ru/
	# 	http://abacaba.com
	# 	http://abacaba.com/test
	# 	http://abacaba.de/
	# 	http://abacaba.ru/test
	# 	http://abacaba.de/test
	# 	http://abacaba.com/
	# 	http://abacaba.com/t
	# 	http://abacaba.com/test
	# 	""".split()
	# addresses = """
	# 	http://c
	# 	http://ccc.bbbb/aba..b
	# 	http://cba.com
	# 	http://a.c/aba..b/a
	# 	http://abc/
	# 	http://a.c/
	# 	http://ccc.bbbb
	# 	http://ab.ac.bc.aa/
	# 	http://a.a.a/
	# 	http://ccc.bbbb/
	# 	http://cba.com/
	# 	http://cba.com/aba..b
	# 	http://a.a.a/aba..b/a
	# 	http://abc/aba..b/a
	# 	""".split()

	import random
	import string

	n = 100000

	addresses = []
	for i in range(n):
		domain = ''.join([random.choice(string.ascii_lowercase) for dummy in range(5)])
		page = ''.join([random.choice(string.ascii_lowercase) for dummy in range(5)])
		addresses.append('http://{}/{}'.format(domain, page))

	print('Solving...')
	s = solve(addresses)
	print(s)


def __starting_point():
	# test()
	main()

__starting_point()
