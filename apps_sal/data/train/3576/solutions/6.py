def longest(words):
    longest=words[0]
    for i in range(len(words)):
        if len(words[i])>len(longest):
            longest = words[i]
    return len(longest)
