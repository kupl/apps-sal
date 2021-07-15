def missing(nums, s):
    try:
        return ''.join(s.replace(' ', '')[i] for i in sorted(nums)).lower()
    except IndexError:
        return 'No mission today'
