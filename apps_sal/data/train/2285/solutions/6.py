T = int(input())
for t in range(T):
    N = int(input())
    sequence = input().strip()
    digits = set(sequence)
    isPossible = False
    number = ""
    ret = []
    for minTwo in digits:
        ret = []
        one = str(0)
        two = minTwo
        for i, digit in enumerate(sequence):
            if digit < one:
                break
            elif digit >= two:
                two = digit
                ret.append("2")
            elif digit > minTwo:
                break
            else:
                one = digit
                ret.append("1")
            if i == len(sequence) - 1:
                isPossible = True
        if isPossible:
            break
    if isPossible:
        ret = "".join(ret)
        print(ret)
    else:
        print("-")

