def palindrome_chain_length(n):
    run = 0
    word = str(n)
    revers = word[::-1]
    while word != revers:
        word = str(int(word) + int(word[::-1]))
        revers = word[::-1]
        run += 1
    return run
