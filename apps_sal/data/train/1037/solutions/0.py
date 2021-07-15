for _ in range(int(input())):
    s = input().strip()
    a = []
    last = 0
    for i in range(len(s)):
     if s[i] == 'P':
      a.append(i - last)
      last = i + 1
    x = 0
    a = a[::-1]
    for v in a[::2]:
     x ^= v % 3
    print('Yes' if x else 'No')
