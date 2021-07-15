def longest(s):
    chunks = []
    for c in s:
        if chunks and chunks[-1][-1] <= c:
            chunks[-1] += c
        else:
            chunks.append(c)
    return max(chunks, key=len)
