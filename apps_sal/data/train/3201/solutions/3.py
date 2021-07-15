def validate_time(time):
    import re
    return bool(re.search(r'^((0\d)|(\d)|(1\d)|(2[0-3])):((0[0-9])|([0-5][0-9]))$',time))
