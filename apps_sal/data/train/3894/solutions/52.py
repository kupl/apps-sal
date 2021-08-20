def count_characters(s):
    """
        Returns 0 if more lowercase, 1 if more uppercase
    """
    uppercase = 0
    lowercase = 0
    for i in range(len(s)):
        if s[i].islower():
            lowercase += 1
        else:
            uppercase += 1
    if uppercase > lowercase:
        return 1
    else:
        return 0


def solve(s):
    if count_characters(s) == 1:
        return s.upper()
    else:
        return s.lower()
