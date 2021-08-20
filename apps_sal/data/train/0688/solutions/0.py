n = int(input())
for i in range(n):
    count = 0
    s = input()
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            count += 1
    if s[0] != s[-1]:
        count += 1
    print('uniform' if count <= 2 else 'non-uniform')
