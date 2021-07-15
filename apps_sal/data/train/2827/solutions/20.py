def switch_it_up(number):
    return __import__('unicodedata').name(str(number)).title()[6:]
