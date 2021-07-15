# write the function is_anagram
def is_anagram(test, original):
    flag = 0
    if len(test) != len(original):
        return False
    else:
        for i in test.lower():
            if i not in original.lower():
                flag = 1
            else:
                continue
        if flag ==1:
            return False
        else:
            return True
