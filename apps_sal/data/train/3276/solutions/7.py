def missing(nums, str):
    try:
        return ''.join([str.replace(' ', '')[i] for i in sorted(nums)]).lower()
    except:
        return 'No mission today'
