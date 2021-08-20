def wallpaper(l, w, h):
    result = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty'}
    wall_area = 1.15 * (2 * l * h + 2 * w * h)
    wallpaper = 0.52 * 10
    to_buy = wall_area / wallpaper
    for (k, v) in result.items():
        if l == 0 or w == 0 or h == 0:
            return 'zero'
        elif int(k) == round(to_buy + 0.5):
            return v
