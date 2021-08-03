for _ in range(int(input())):
    s = input()
    n = len(s)
    decode = [0] * (n + 1)
    if s[0] == '0':
        print(0)
        continue

    decode[0] = 1
    decode[1] = 1
    modul = 1000000007
    for i in range(2, n + 1):
        if s[i - 1] > '0':
            decode[i] = (decode[i] % modul + decode[i - 1] % modul) % modul

        if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] < '7'):
            decode[i] = (decode[i] % modul + decode[i - 2] % modul) % modul

    print(decode[n])
