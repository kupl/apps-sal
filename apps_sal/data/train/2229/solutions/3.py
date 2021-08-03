
def main():
    a_string = input()
    b_string = input()
    moves = [int(x) for x in input().split()]
    index_of_move = {}
    lenb = len(b_string)

    for index, elem in enumerate(moves):
        index_of_move[elem] = index + 1

    l = 0
    r = len(moves) - 1
    while l < r:
        middle = int((l + r + 1) / 2)
        bi = 0
        i = 0

        for index, elem in enumerate(a_string):
            # if (index + 1) in moves[:(middle + 1)]:
            #  continue
            if index_of_move[index + 1] <= middle + 1:
                continue
            if elem is b_string[bi]:
                bi += 1
            if bi >= lenb:
                break

        if bi >= lenb:
            l = middle
        else:
            r = middle - 1

    if l is 0 and r is 0:
        bi = 0
        for index, elem in enumerate(a_string):
            if index_of_move[index + 1] <= 1:
                continue
            if elem is b_string[bi]:
                bi += 1
            if bi >= lenb:
                break
        if bi >= lenb:
            print(1)
        else:
            print(0)
    else:
        print(l + 1)


def __starting_point():
    main()


__starting_point()
