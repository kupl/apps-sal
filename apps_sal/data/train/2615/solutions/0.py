import re
n = int(input())
for i in range(n):
    s = input()
    search_result = re.search('^[+-]?\\d*\\.\\d+$', s)
    print(bool(search_result))
