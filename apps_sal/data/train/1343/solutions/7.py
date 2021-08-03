import sys

n = int(input())

for i in range(n):

    s = input()
    m = len(s)

    if (m == 1):
        sys.stdout.write('NO\n')

    elif (m % 2 != 0):

        # check left half
        i = 0
        j = int(m / 2) + 1
        flag = False
        Flag = True
        while (j < m):
            # print(i,j)
            if (s[i] != s[j]):
                if (not flag):
                    flag = True
                    i += 1
                else:
                    Flag = False
                    break
            else:
                i += 1
                j += 1

        if (not Flag):

            # check right half
            i = 0
            j = int(m / 2)
            flag = False
            Flag = True
            while (j < m):
                # print(i,j)
                if (s[i] != s[j]):
                    if (not flag):
                        flag = True
                        j += 1
                    else:
                        Flag = False
                        break
                else:
                    i += 1
                    j += 1
            if (Flag):
                sys.stdout.write('YES\n')
            else:
                sys.stdout.write('NO\n')

        else:
            sys.stdout.write('YES\n')

    else:
        if (s[:int(m / 2)] == s[int(m / 2):]):
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')
