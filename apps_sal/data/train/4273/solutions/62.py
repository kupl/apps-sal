def shorten_to_date(long_date):
    return ' '.join(long_date.split(' ')[:3]).replace(',', '')
    # output joins a string that been split from the input, consists of the first 3 elements, and removes the ,

