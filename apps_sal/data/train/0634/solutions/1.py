def main():
    res = 0
    ind = 0
    curr = []
    letterflag = False

    chars = list(input())

    for c in chars:
        if c.isalpha():
            if letterflag:
                val = int(''.join(curr))
                res = max(res, val)
                curr = curr[ind:]
            else:
                letterflag = True

            curr.append("9")
            ind = len(curr)

        else:
            curr.append(c)

    # Last call
    val = int(''.join(curr))
    res = max(res, val)
    print(res)


main()
