test_cases = int(input())

for _ in range(test_cases):
    s = input()
    ans = 0
    s += '0'
    index = s.index('0')
    if index == 0 or index == len(s)-1:
        print(ans)
    else:
        for i in range(index, len(s)-1):
            if s[i] == '0':
                ans += 1
            else:
                break
        print(ans)
