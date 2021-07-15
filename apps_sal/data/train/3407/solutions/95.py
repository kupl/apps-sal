def palindrome_chain_length(n):
    answer = []
    pal = int(str(n)[::-1])
    while n != pal:
        n += pal
        pal = int(str(n)[::-1])
        answer.append(n)
    return len(answer)
