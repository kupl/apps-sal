def main():
    rev_s = reversed(input())
    flips = 0
    flipped = False
    for b in rev_s:
        if b == '0':
            if not flipped:
                continue
            else:
                flipped = False
                flips += 1
                continue
        elif flipped:
            continue
        else:
            flipped = True
            flips += 1
            continue
    print(flips)


main()
