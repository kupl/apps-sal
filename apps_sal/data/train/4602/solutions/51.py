def is_anagram(test, original):
    counterTest = [0] * 255
    counterOri = [0] * 255
    for i in range(len(test)):
        counterTest[ord(test[i].lower())] += 1
    for i in range(len(original)):
        counterOri[ord(original[i].lower())] += 1
    if counterOri == counterTest:
        return True
    else:
        return False
