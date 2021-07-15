def numericals(line):
    
    counts = dict.fromkeys(line, 0)
    output = []
    for char in line:
        counts[char] += 1
        output.append(counts[char])

    return ''.join(str(number) for number in output)
