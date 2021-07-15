import re
def reverseWords(str):
    return "".join(re.split(r'(\s+)', str)[::-1])
