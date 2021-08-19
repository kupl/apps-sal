# 1 technique using replace
def solution(string):

    # feed string characters in reverse, see for loop below
    stringReversal = []
    # will hold final reverse string
    somaReverseString = ''

    for i in range(len(string)):
        # replace the forward character order in reverse
        migratingCharacter = string.replace(string[i], string[-i - 1])
        # append the newly replaced character to stringReversal
        # captures reverse ordering
        stringReversal.append(migratingCharacter[i])
        # undo the replacement, to prevent copying over the original string
        string.replace(string[i], string[-i - 1])

    # now stringReversal holds the string characters in reverse, as list items

    for i in stringReversal:
        somaReverseString += i
    return somaReverseString


# 2 more direct proof, skips the replace,
# feeds reverse ordering directly to the list
def solution(string):
    strings = []
    soma = ''
    stringLengthRange = list(range(len(string)))
    for i in stringLengthRange:
        # index from start is 0, index from end is -1, -
        # - 1 from stringLengthRange offsets this
        strings.append(string[-i - 1])
    for i in strings:
        soma += i
    return soma


# 3 here is the index-slicing one-liner
def solution(string):
    return string[::-1]
