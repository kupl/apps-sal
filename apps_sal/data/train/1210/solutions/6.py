# cook your dish here
t = int(input())

for i in range(t):
    nx = [int(i) for i in input().split()][:2]
    direct_lang = [(i) for i in input().split()][:2]
    n = nx[0]
    x = nx[1]
    direct = direct_lang[0]
    language = direct_lang[1]

    if(direct == 'L'):
        number_is = x
        index = x - 1
        if(index % 2 == 0):
            language_is = language
        else:
            if(language == 'H'):
                language_is = 'E'
            else:
                language_is = 'H'

    else:
        number_is = (n - x) + 1
        index = x - 1
        if((n - 1) % 2 == 0):
            if(index % 2 == 0):
                language_is = language
                # print('1')
            else:
                if(language == 'H'):
                    language_is = 'E'
                    # print('0')
                else:
                    language_is = 'H'
                    # print('0')

        else:
            if(index % 2 != 0):
                language_is = language
                # print('1')
            else:
                if(language == 'H'):
                    language_is = 'E'
                    # print('0')
                else:
                    language_is = 'H'
                    # print('0')
    print(str(number_is) + ' ' + str(language_is))
