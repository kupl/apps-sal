import re


def remove_chars(s):
    s = re.sub('\\W+', ' ', re.sub('[^A-Za-z]+', '', re.sub('[\\s]', 'SSSSSSSSSS', s)))
    return re.sub('[S]{10}', ' ', s)
