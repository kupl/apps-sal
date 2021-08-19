a = int(input())
for i in range(a):
    r = int(input())
    s = input()
    score = 0
    count = 0
    for i in range(len(s)):
        if s[i] == ')':
            score -= 1
            if score < 0:
                score = 0
                count += 1
        else:
            score += 1
    print(count)
