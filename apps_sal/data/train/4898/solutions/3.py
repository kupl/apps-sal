import re


def digit_all(x):
    try:
        return re.sub('[^\\d]*', '', x)
    except:
        return 'Invalid input !'
