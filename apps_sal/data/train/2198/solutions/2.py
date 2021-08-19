import sys
n = int(input())
s = set()
for line in sys.stdin:
    prev = line
    while True:
        word = prev.strip().replace('oo', 'u').replace('kh', 'h').replace('uo', 'ou')
        if prev == word:
            break
        else:
            prev = word
    s.add(prev)
print(len(s))
