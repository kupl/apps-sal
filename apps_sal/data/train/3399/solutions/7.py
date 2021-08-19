def alpha_seq(string):
    (memo, output) = ({}, [])
    for char in sorted(string.lower()):
        if char not in memo:
            memo[char] = char.upper() + char * (ord(char) - 97)
        output.append(memo[char])
    return ','.join(output)
