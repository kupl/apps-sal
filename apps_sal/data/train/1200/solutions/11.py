n = int(input())
while n != 0:
    i = 0
    flag = True
    string = input()
    while i <= (len(string) - 2):
        if string[i] == string[i + 1]:
            print('no')
            flag = False
            break
        else:
            i += 2
    if flag == True:
        print('yes')
    n -= 1
