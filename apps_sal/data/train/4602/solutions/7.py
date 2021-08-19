def is_anagram(test, original):
    if len(test) != len(original):
        return False
    alphabet = [0] * 26
    for i in range(len(test)):
        alphabet[(ord(test[i]) & 31) - 1] += 1
        alphabet[(ord(original[i]) & 31) - 1] -= 1
    return not any(alphabet)
