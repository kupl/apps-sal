import re
def dollar_to_speech(val):
    if '-' in val: return 'No negative numbers are allowed!'
    c =  int(re.findall(r'\.(\d+)',val)[0])
    d = int(re.findall(r'\$(\d+)\.',val)[0])
    if d == 0 == c : return '0 dollars.'
    
    seg1 = '{} dollar{}'.format(d,('s' if d > 1 else '')) if d else ''
    seg2 = '{} cent{}'.format(c,  ('s' if c > 1 else '')) if c else ''
    seg3 = ' and ' if seg1 and seg2 else ''
    return ''.join([seg1,seg3,seg2,'.'])
    
    

