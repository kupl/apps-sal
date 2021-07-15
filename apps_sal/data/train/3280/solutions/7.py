def make_readable(seconds):
    '''Returns the time in `seconds` as a human-readable format (HH:MM:SS).
    '''
    minute, hour = 60, 60 ** 2    
    return "%02d:%02d:%02d" % (
        seconds / hour,
        seconds % hour / minute,
        seconds % hour % minute
    )
