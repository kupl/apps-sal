import re


def parse_float(string):
    if not isinstance(string, str):
        return None 
    
    res = re.match(r'[0-9.]+', string)
    return float(res.group()) if res else None
