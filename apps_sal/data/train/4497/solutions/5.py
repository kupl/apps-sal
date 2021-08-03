def positive_to_negative(binary):
    b = []

    print("원래 이진수 :", binary)
    # range(1, 5) 1, 2, 3, 4
    for bit in binary:
        if bit == 1:
            b.append(0)
        else:
            b.append(1)
    print("1과 0 바꾸기 :", b)

    c = 1
    for i in range(len(b)):
        if b[-1 - i] == 1 and c == 1:
            b[-1 - i] = 0
        elif b[-1 - i] == 0 and c == 1:
            c = 0
            b[-1 - i] = 1
        else:
            pass

    """
    b.reverse()
    print("배열 순서 바꾸기 :",b)
    
    c = 1
    for i in range(len (b)):
        if b[i] == 1 and c == 1:
            b[i] = 0
        elif b[i] == 0 and c == 1:
            c = 0
            b[i] = 1
        else:
            pass
        
    print(b)
    b.reverse()        """
    print("최종 :", b)

    return b
