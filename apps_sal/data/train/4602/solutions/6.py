def is_anagram(test, original):
    if len(test) != len(original):
        return False

    count = [0] * 26

    for i in range(len(test)):
        count[(ord(test[i]) & 31) - 1] += 1
        count[(ord(original[i]) & 31) - 1] -= 1

    return not any(count)
