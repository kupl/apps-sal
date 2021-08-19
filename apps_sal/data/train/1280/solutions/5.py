t = int(input())
lst = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(t):
    s = list(input().strip())
    count = 0
    s.insert(0, 'temp')
    for i in range(1, len(s)):
        if i > len(s) // 2:
            break
        if s[i] != s[-i]:
            count += abs(lst.index(s[i]) - lst.index(s[-i]))
    print(count)
