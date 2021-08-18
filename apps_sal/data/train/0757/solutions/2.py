def isVowel(z):
    if z == 'A' or z == 'E' or z == 'I' or z == 'O' or z == 'U':
        return True
    else:
        return False


t = int(input())
for i in range(t):
    n = int(input())
    strr = input().strip()
    flag = 0
    vol = list(strr)
    if n > 1:
        if isVowel(strr[0]) and isVowel(strr[-1]):
            print("Yes")
            continue
        else:
            for j in range(n - 1):
                if isVowel(strr[j]) and isVowel(strr[j + 1]):
                    print("Yes")
                    flag = 1
                    break
    if flag == 0:
        print("No")
