# Stack solution:
#    Loop through s2 once, pushing char occurances onto the stack
#    Loop through s1 once, popping any occurances of s2 chars from the stacks
#    If any stack has a count greater than 0, than it's False
def scramble(s1, s2):
    stacks = {}
    
    for char in s2:
        # Checking if stacks already has a key:value pair with the key char
        if char in stacks:
            stacks[char] += 1
        else:
            stacks[char] = 1
    
    for char in s1:
        if char in stacks:
            stacks[char] -= 1
  
    return max(stacks.values()) <= 0

'''
# Turn strings into lists, remove the appropriate element, and keep track of it to compare at the end
# Takes too long, but correct output
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
# Turn strings into lists, remove the appropriate element, and catch ValueError exceptions that signify False-ness
# Takes too long but correct output
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
# Count every instance of every char in s1 and s2, then compare the number of s2 char appearances in s1
# slowest of all three
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
