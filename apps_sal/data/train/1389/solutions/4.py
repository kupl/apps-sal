import re
n = int(input(''))
m = n - 1
lst = list()
while n > 0:
    tmp = re.sub(r'[^\w\s]', '', input('')).split()
    lst.append(tmp[::-1])
    n = n - 1

while m >= 0:
    print(*lst[m], sep=" ")
    m = m - 1
