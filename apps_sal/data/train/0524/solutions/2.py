
string = input()
token = {}
for i in range(98, 123, 2):
    token[chr(i)] = 0
l = [token.copy()]
for letter in string:
    if (ord(letter) + 1) % 2:
        token[letter] += 1
    l.append(token.copy())
q = int(input())
for query in range(q):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    ans = 0
    if a > len(string):
        a = len(string)
    if b > len(string):
        b = len(string)
    if a < 1:
        a = 1
    if b < 1:
        b = 1
    for i in range(98, 123, 2):
        if l[b][chr(i)] > l[a - 1][chr(i)]:
            ans += 1
    print(ans)
