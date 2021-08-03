def time_correct(t):
    if t is None or len(t) == 0:
        return t
    nums = t.split(":")
    if len(nums) != 3:
        return None
    for num in nums:
        if not num.isdigit():
            return None
    hour, min, sec = [int(x) for x in nums]
    if sec > 59:
        min += (sec / 60)
        sec %= 60
    if min > 59:
        hour += (min / 60)
        min %= 60
    if hour > 23:
        hour %= 24
    return "%02d:%02d:%02d" % (hour, min, sec)
