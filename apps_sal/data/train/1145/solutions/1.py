import sys


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n % 2 == 0:
            print('0')
        else:
            str = ''
            possible = 1
            while n != 1:
                if (n - 1) / 2 % 2 == 1:
                    n = n - 1
                    n = n / 2
                    str += '2'
                elif (n + 1) / 2 % 2 == 1:
                    n += 1
                    n = n / 2
                    str += '1'
                else:
                    possible = 0
            if not possible:
                print('0')
            else:
                output = ''
                for j in range(len(str)):
                    output += str[len(str) - j - 1]
                print(output)


main()
