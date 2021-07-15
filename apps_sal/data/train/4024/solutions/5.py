import re
def special_number(number):
    return "Special!!" if re.match(r'^[0-5]+$', str(number)) else "NOT!!" 
