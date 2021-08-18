i = 0
test_num = eval(input())
while i < test_num:
    r = 0
    index = 0
    new_inp = 0
    inp = input()
    inp_list = list(inp)
    for digit in reversed(inp_list):
        d = int(digit)
        if index % 6 == 0:
            r = r + d * 1
        if index % 6 == 1:
            r = r + d * 3
        if index % 6 == 2:
            r = r + d * 2
        if index % 6 == 3:
            r = r + d * 6
        if index % 6 == 4:
            r = r + d * 4
        if index % 6 == 5:
            r = r + d * 5
        index += 1
        r = r % 7
    if r == 0:
        print(inp)
    else:
        if r % 4 == 0:
            print(int(inp) - r)
        else:
            new_inp = int(inp) - r
            j = 1
            while True:
                if new_inp == 0:
                    print("-1")
                    break
                elif r + j * 7 < int(inp):
                    if (r + j * 7) % 4 == 0:
                        print(new_inp - j * 7)
                        break
                else:
                    print("-1")
                    break
                j += 1
    i += 1
