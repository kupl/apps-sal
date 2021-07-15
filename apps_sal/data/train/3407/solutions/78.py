def palindrome_chain_length(n):
    steps = 0
    string = str(n)
    while string != string[::-1]:
        n += int(string[::-1])
        string = str(n)
        steps += 1
    return steps
