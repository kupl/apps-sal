
def main():
    s = input()
    l = len(s)

    pretty_count = 0
    for i in range(l):
        left_paren_count = 0
        right_paren_count = 0
        wild_count = 0
        for j in range(i, l):
            if s[j] == '(':
                left_paren_count += 1
            elif s[j] == ')':
                right_paren_count += 1
            else:
                wild_count += 1

            if left_paren_count + wild_count < right_paren_count:
                break
            if left_paren_count < wild_count + right_paren_count:
                wild_count -= 1
                left_paren_count += 1
                if wild_count < 0:
                    break
            if left_paren_count == wild_count + right_paren_count:
                pretty_count += 1
    print(pretty_count)


def __starting_point():
    main()


__starting_point()
