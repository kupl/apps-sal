def could_be(original, another):
    import unicodedata
    import re
    import numpy as np
    if len(original) == 0:
        return False
    temp = u''.join([ii for ii in unicodedata.normalize('NFKD', another) if not unicodedata.combining(ii)])
    temp = re.sub('[!,;:.?]', ' ', temp).lower()
    temp = re.sub(' +', ' ', temp)
    if temp.strip() == original.lower():
        return True
    elif np.sum(np.isin(np.array(original.lower().split(' ')), np.array(temp.split(' ')))) == len(temp.split(' ')):
        return True
    return False
