(a, b) = (input(), input())
ax = sum([ord(c) - ord('0') for c in a])
bx = sum([ord(c) - ord('0') for c in b])
print('YES' if bx <= ax + ax % 2 else 'NO')
