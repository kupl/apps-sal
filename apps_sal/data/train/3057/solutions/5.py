def is_bouncy(number):
    string = str(number)
    sort = "".join(sorted(string))
    reverse = "".join(reversed(string))
    return sort != string and sort != reverse
