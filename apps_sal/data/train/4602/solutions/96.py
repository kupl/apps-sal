# write the function is_anagram
def is_anagram(test, original):
    org1 = [x.lower() for x in original]
    org2 = [y.lower() for y in test]
    org1.sort()
    org2.sort()
    if org1 == org2:
        return True
    return False
