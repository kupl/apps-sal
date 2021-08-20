testcases = int(input())
alphabet = 'aiemckgobjfndlhp'
for testcase in range(testcases):
    length = int(input())
    code = input()
    string = ''
    for byte in range(0, length, 4):
        letter = code[:4]
        num = int(code[3]) * 8 + int(code[2]) * 4 + int(code[1]) * 2 + int(code[0])
        string += alphabet[num]
        code = code[4:]
    print(string)
