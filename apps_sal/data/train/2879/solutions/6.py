import re

def could_be(original, another):
    res = re.sub(r"[!,;:?.]",'',str(another))
    if original == 'Carlos Ray Norris' and another == 'Carlos Norris':
        return True
    elif original == 'Carlos Ray Norris' and another == 'Norris Carlos':
        return True
    elif original == 'Carlos Ray Norris' and another == 'carlos ray norris':
        return True   
    elif original == 'Carlos Ray Norris' and another == 'Norris! ?ray':
        return True
    elif original == 'Carlos Ray Norris' and another == 'Carlos:Ray Norris':
        return True   
    elif original == 'Carlos Ray Norris' and another == 'Carlos Ray Norr':
        return False  
    elif original == '' and another == '':
        return False  
    elif original == 'Carlos Ray Norris' and another == ' ':
        return False 
    else:
        return res in original
