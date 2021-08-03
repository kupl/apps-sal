# cook your dish here
def f(n):
    count = 1
    if n % 2 == 0:
        for i in range(1, n // 2 + 1):
            if i == n // 2:
                count += 1
            else:
                count += n - i
        return count
    else:
        for i in range(1, n // 2 + 1):
            count += n - i
        return count


s = input()
c, count = 1, 0
lst = []
if 'c' in s or 'k' in s:
    print(0)
    return
for i in range(len(s) - 1):
    if s[i] == s[i + 1] == 'g':
        count += 1
    elif s[i] == s[i + 1] == 'f':
        count += 1
    else:
        if count:
            lst.append(count + 1)
            count = 0
if count:
    lst.append(count + 1)
# print(lst)
for i in lst:
    c = c * (f(i))
    # print(f(i))
print(c)
