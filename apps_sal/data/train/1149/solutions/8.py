test = int(input())
for _ in range(test):
    strText = input()
    n = len(strText)
    ans = 1
    rangeCheck = n
    if(n % 2 == 0):
        rangeCheck = rangeCheck // 2
    else:
        rangeCheck = rangeCheck // 2 + 1

    if(len(strText) == strText.count('?')):
        ans = (ans * (26**rangeCheck)) % (10**7 + 9)
    else:
        for i in range(rangeCheck):
            start = strText[i]
            end = strText[n - 1 - i]
            if(start == '?' and end == '?'):
                ans = (ans * 26) % (10**7 + 9)
            else:
                if(start != end):
                    if(start != '?' and end != '?'):
                        ans = 0
                        break
    print(ans)  # just code here
