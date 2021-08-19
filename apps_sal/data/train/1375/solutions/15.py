for _ in range(eval(input())):
    string = input()
    string = string[::-1]
    for i in range(len(string)):
        if string[i] != '0':
            break
    print(string[i:])
