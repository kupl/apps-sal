import re


def get_count(words=''):
    (vow_count, con_count) = (0, 0)
    if type(words) is str:
        (remainder, vow_count) = re.subn('[aeiou]', '', words, flags=re.I)
        (_, con_count) = re.subn('\\w', '', remainder, flags=re.I)
    return {'vowels': vow_count, 'consonants': con_count}
