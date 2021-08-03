t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    l = ['A', 'E', 'I', 'O', 'U']
    if n < 2:
        print('No')
    elif 'A' in s or 'E' in s or 'I' in s or 'O' in s or 'U' in s:
        if ('AA' in s) or ('AE' in s) or ('AI' in s) or 'AO' in s or 'AU' in s:
            print('Yes')
        elif 'EA' in s or 'EE' in s or 'EI' in s or 'EO' in s or 'EU' in s:
            print('Yes')
        elif 'IA' in s or 'IE' in s or 'II' in s or 'IO' in s or 'IU' in s:
            print('Yes')
        elif 'OA' in s or 'OE' in s or 'OI' in s or 'OO' in s or 'OU' in s:
            print('Yes')
        elif 'UA' in s or 'UE' in s or 'UI' in s or 'UO' in s or 'UU' in s:
            print('Yes')
        elif (s[0] in l) and (s[n - 1] in l):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
