import re
s = input()
res = re.search('([A-Za-z0-9])\\1', s)
if res == None:
    print(-1)
else:
    print(res.group(1))
