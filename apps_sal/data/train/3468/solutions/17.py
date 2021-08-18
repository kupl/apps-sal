def scramble(s1, s2):
    stacks = {}

    for char in s2:
        if char in stacks:
            stacks[char] += 1
        else:
            stacks[char] = 1

    for char in s1:
        if char in stacks:
            stacks[char] -= 1

    return max(stacks.values()) <= 0


'''
def scramble(s1, s2):
    source = [char for char in s1]
    tokens = [char for char in s2]
    result = []
    
    for char in tokens:
        if char in source:
            result.append(char)
            source.remove(char)
    return len(result) == len(tokens)
'''

'''
def scramble(s1, s2):
    source = [char for char in s1]
    try:
        for char in s2:
            source.remove(char)
    except ValueError:
        return False
    return True
'''

'''
def scramble(s1, s2):
    source = [char for char in s1]
    source.sort()
    tokens = [char for char in s2]
    tokens.sort()
    
    source_len = len(source)
    source_index = 0
    for char in tokens:
        while char != source[source_index]:
            source_index += 1
            if source_index >= source_len:
                return False
    return True
'''
