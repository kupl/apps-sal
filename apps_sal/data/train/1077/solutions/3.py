a = int(eval(input()))
for i in range(0, a):
    n = eval(input())
    k = n
    word = []
    for j in range(0, n):
        t = input()
        word.append(t)
        l = []
    flag = 0
    for j in range(k - 1, -1, -1):
        l = word[j].split()

        if(j == k - 1):
            print("Begin", end=' ')
        elif(right == 0):
            print("Right", end=' ')
        elif(right == 1):
            print("Left", end=' ')

        if(l[0] == 'Left'):
            right = 0
        elif(l[0] == 'Right'):
            right = 1
        for index in range(1, len(l) - 1):
            print(l[index], end=' ')
        print(l[index + 1])
    print()
