import re
def generate_hashtag(s):
    return '#' + (''.join(re.findall('[A-Za-z]', s.title()))) if 0 < len(s) < 140  else False
