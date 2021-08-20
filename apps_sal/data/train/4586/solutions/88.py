remote = ['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/']


def tv_remote(word):
    current = find_char('a')
    result = 0
    for character in word:
        new = find_char(character)
        result += sum([abs(current[0] - new[0]), abs(current[1] - new[1])]) + 1
        current = new
    return result


def find_char(char):
    for col in range(0, len(remote)):
        if char in remote[col]:
            return [col, remote[col].find(char)]
