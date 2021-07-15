def wallpaper(l, w, h):
    from math import ceil
    
    num_words_dic = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', \
            18: 'eighteen', 19: 'nineteen', 20: 'twenty'}
    S_wall = (l + w) * 2 * h
    S_paper = 5.2 
    
    return "zero" if l*w*h == 0 else num_words_dic[ceil(S_wall / S_paper * 1.15)]
