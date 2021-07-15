def switch_it_up(number):
    import unicodedata
    return unicodedata.name(str(number)).split(None)[1].title()
