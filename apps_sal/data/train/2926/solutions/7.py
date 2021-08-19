def reverse(a):
    letters = ''.join(a)[::-1]
    (result, chunk_size) = ([], 0)
    for word in a:
        result.append(letters[chunk_size:chunk_size + len(word)])
        chunk_size += len(word)
    return result
