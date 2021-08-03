for _ in range(int(input())):

    n, k = map(int, input().split())

    s = ''

    lista = list(map(int, input().split()))

    for i in lista:

        if(i % k == 0):

            s += '1'

        else:

            s += '0'

    print(s)
