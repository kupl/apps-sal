def de_nico(key, msg):
    sorted_key = sorted(key)
    num_key = []
    for chr in key:
        num_key.append(sorted_key.index(chr))

    result = ''
    start = 0
    end = len(key)
    while start < len(msg):
        chunk = msg[start: end]
        for index in num_key:
            if index < len(chunk):
                result += chunk[index]
        start = end
        end += len(key)

    return result.strip()
