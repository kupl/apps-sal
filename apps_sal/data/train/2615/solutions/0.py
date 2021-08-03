import re
n = int(input())
for i in range(n):
    s = input()
    search_result = re.search(r'^[+-]?\d*\.\d+$', s)
    print((bool(search_result)))
