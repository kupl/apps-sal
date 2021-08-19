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


'\n# Turn strings into lists, remove the appropriate element, and keep track of it to compare at the end\n# Takes too long, but correct output\ndef scramble(s1, s2):\n    source = [char for char in s1]\n    tokens = [char for char in s2]\n    result = []\n    \n    for char in tokens:\n        if char in source:\n            result.append(char)\n            source.remove(char)\n    return len(result) == len(tokens)\n'
'\n# Turn strings into lists, remove the appropriate element, and catch ValueError exceptions that signify False-ness\n# Takes too long but correct output\ndef scramble(s1, s2):\n    source = [char for char in s1]\n    try:\n        for char in s2:\n            source.remove(char)\n    except ValueError:\n        return False\n    return True\n'
'\n# Count every instance of every char in s1 and s2, then compare the number of s2 char appearances in s1\n# slowest of all three\ndef scramble(s1, s2):\n    source = [char for char in s1]\n    source.sort()\n    tokens = [char for char in s2]\n    tokens.sort()\n    \n    source_len = len(source)\n    source_index = 0\n    for char in tokens:\n        while char != source[source_index]:\n            source_index += 1\n            if source_index >= source_len:\n                return False\n    return True\n'
