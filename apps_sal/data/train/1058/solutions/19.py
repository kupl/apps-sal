for _ in range(int(input())):
    digits = list(input())
    (inc, out) = (0, '')
    while inc < len(digits):
        out += str(int(digits[inc]) - 2)
        inc += 1
    print(out)
