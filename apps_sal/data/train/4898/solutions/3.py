import re
def digit_all (x):
    try:
        return re.sub(r'[^\d]*','',x)
    except:
        return 'Invalid input !'
