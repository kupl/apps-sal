# cook your dish here
try:
    test_cases = int(input())
    for _ in range(test_cases):
        n, k = input().split()
        dictOfForgottenWord = list(input().split())
        modernDict = ''
        for i in range(int(k)):
            modernDict += " " + input()

        newModernDict = list(set(list(modernDict.split(" "))))

        for i in dictOfForgottenWord:
            if i in newModernDict:
                print("YES", end=' ')
            else:
                print("NO", end=' ')
        print()

except:
    pass
