from decimal import *

def color_probability(color, texture):
    bag_content = {
        ("red", "smooth"): 1,
        ("red", "bumpy"): 4,
        ("yellow", "bumpy"): 2,
        ("yellow", "smooth"): 1,
        ("green", "bumpy"): 1,
        ("green", "smooth"): 1,
    }

    color_match_number = Decimal(bag_content[color, texture])
    
    texture_match_list = [bag_content[k] for k in bag_content.keys() if k[1]==texture]
    texture_match_number =  Decimal(sum(texture_match_list))
    
    return str(Decimal(color_match_number/texture_match_number).quantize(Decimal('.01'), rounding=ROUND_DOWN))
