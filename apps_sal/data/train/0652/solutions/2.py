def compare(a, b):
    return ord(a.lower()) - ord(b.lower())


for test in range(eval(input())):
    A = input()
    B = input()

    length = len(A)
    diff = 0

    for i in range(length):
        diff = compare(A[i], B[i])
        if(diff == 0):
            continue
        else:
            break

    if(diff < 0):
        print("first")
    elif(diff > 0):
        print("second")
    else:
        print("equal")
