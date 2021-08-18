test = int(input())
for t in range(test):
    s = input()
    prev = s[0]
    total = 0
    count = 0
    for i in s:
        if i == prev:
            count += 1
        else:
            if(count == 0 or count == 1):
                total += 8
            else:
                total += 40
            count = 1
        prev = i

    if(s[len(s) - 1] == s[len(s) - 2]):
        total += 40
    else:
        total += 8
    diff = (len(s) * 8) - (total)
    print(diff)
