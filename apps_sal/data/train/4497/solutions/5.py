def positive_to_negative(binary):
    b = []
    print('원래 이진수 :', binary)
    for bit in binary:
        if bit == 1:
            b.append(0)
        else:
            b.append(1)
    print('1과 0 바꾸기 :', b)
    c = 1
    for i in range(len(b)):
        if b[-1 - i] == 1 and c == 1:
            b[-1 - i] = 0
        elif b[-1 - i] == 0 and c == 1:
            c = 0
            b[-1 - i] = 1
        else:
            pass
    '\n    b.reverse()\n    print("배열 순서 바꾸기 :",b)\n    \n    c = 1\n    for i in range(len (b)):\n        if b[i] == 1 and c == 1:\n            b[i] = 0\n        elif b[i] == 0 and c == 1:\n            c = 0\n            b[i] = 1\n        else:\n            pass\n        \n    print(b)\n    b.reverse()        '
    print('최종 :', b)
    return b
