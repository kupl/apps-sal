import re
def increment_string(strng):
    return strng.replace(re.search('[0-9]*$',strng).group(),'')+str(int(0 if re.search('[0-9]*$',strng).group()=='' else re.search('[0-9]*$',strng).group())+1).rjust(len(re.search('[0-9]*$',strng).group()),'0')

