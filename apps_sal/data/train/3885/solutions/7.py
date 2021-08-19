def values(limit):
    palindromes = set()
    for sequence_item in range(1, int(limit ** 0.5)):
        squares_sum = sequence_item ** 2
        while squares_sum < limit:
            sequence_item += 1
            squares_sum += sequence_item ** 2
            if str(squares_sum) == str(squares_sum)[::-1] and squares_sum < limit:
                palindromes.add(squares_sum)
    return len(palindromes)
