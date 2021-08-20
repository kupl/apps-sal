for _ in range(int(input())):
    l = int(input())
    s = input()
    string = 'abcdefghijklmnop'
    decode = ''
    for b in range(0, l, 4):
        string = 'abcdefghijklmnop'
        for a in range(b, b + 4):
            if s[a] == '0':
                n = len(string) // 2
                string = string[0:n]
            elif s[a] == '1':
                n = len(string)
                string = string[n // 2:n]
        decode = decode + string
    print(decode)
