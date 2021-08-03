def solution(to_cur, value):
    r = []
    for number in value:
        if to_cur == "USD":
            r.append("${:,.2F}".format(number * 1.1363636))
        else:
            r.append("{:,.2F}€".format(number / 1.1363636))
    return r
