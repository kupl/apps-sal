for _ in range(int(input())):
    code = input().strip() + '0'
    message = ''
    asc = int(code[0])

    for i in range(len(code) - 1):

        if int(str(asc) + code[i + 1]) > 256:
            message += chr(asc)
            asc = int(code[i + 1])
        else:
            asc = int(str(asc) + code[i + 1])

    print(message)
