t = int(input())
for i in range(t):
    s = input()
    ans = False
    for j in range(len(s) - 2):
        if(s[j] == '0'):
            if(s[j + 1] == '1'):
                if(s[j + 2] == '0'):
                    ans = True
                    break
        else:
            if(s[j + 1] == '0'):
                if(s[j + 2] == '1'):
                    ans = True
                    break
    if(ans):
        print("Good")
    else:
        print("Bad")
