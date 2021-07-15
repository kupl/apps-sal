import re
def lowercase_count(strng):
    match = re.findall("[a-z]", strng)
    count = 0
    for i in match:
        count +=1
    return count
