a = ord('a')
h = ord('h')

N = int(input())
for x in range(N):
    lines = input()
    if (len(lines) == 5 and lines[2] == '-'):
        try:
            I1 = ord(lines[0])
            I2 = int(lines[1])
            F1 = ord(lines[3])
            F2 = int(lines[4])
            # print I1,I2,F1,F2
            if (a <= F1 <= h and a <= I1 <= h and 1 <= F2 <= 8 and 1 <= I2 <= 8):
                D2 = abs(I2 - F2)
                D1 = abs(F1 - I1)
                #   print D2,D1
                if((D1 == 1 and D2 == 2) or (D1 == 2 and D2 == 1)):
                    print("Yes")
                else:
                    print("No")
            else:
                print("Error")
        except ValueError:
            print("Error")
    else:
        print("Error")
