def bishop_diagonal(bishop1, bishop2):

    rank, file = ord(bishop1[0]) - ord(bishop2[0]), int(bishop1[1]) - int(bishop2[1])

    if abs(rank) == abs(file):

        ranksign, filesign = -1 if rank < 0 else 1, -1 if file < 0 else 1

        while bishop1[0] not in "ah" and bishop1[1] not in "18":
            bishop1 = chr(ord(bishop1[0]) + ranksign) + str(int(bishop1[1]) + filesign)

        while bishop2[0] not in "ah" and bishop2[1] not in "18":
            bishop2 = chr(ord(bishop2[0]) - ranksign) + str(int(bishop2[1]) - filesign)

    return sorted([bishop1, bishop2])
