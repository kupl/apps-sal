testcases = int(input())
while testcases:
    n = int(input())
    print(sum([int(digit) for digit in str(2**n)]))
    testcases -= 1
