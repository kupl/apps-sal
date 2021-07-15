def stat(strg):

    def get_time(s):
        '''Returns the time, in seconds, represented by s.'''
        hh, mm, ss = [int(v) for v in s.split('|')]
        return hh * 3600 + mm * 60 + ss
    
    def format_time(time):
        '''Returns the given time as a string in the form "hh|mm|ss".'''
        hh = time // 3600
        mm = time // 60 % 60
        ss = time % 60
        return '{hh:02d}|{mm:02d}|{ss:02d}'.format(**locals())
    
    def get_range(times):
        return times[-1] - times[0]
    
    def get_average(times):
        return sum(times) // len(times)
    
    def get_median(times):
        middle = len(times) >> 1
        return (times[middle] if len(times) & 1 else
                (times[middle - 1] + times[middle]) // 2)
    
    if strg == '':
        return strg
    times = [get_time(s) for s in strg.split(', ')]
    times.sort()
    rng = format_time(get_range(times))
    avg = format_time(get_average(times))
    mdn = format_time(get_median(times))
    return 'Range: {rng} Average: {avg} Median: {mdn}'.format(**locals())
