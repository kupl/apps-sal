def shorten_to_date(long_date):
    broken = long_date.split(" ")
    date = str(broken[2]).strip(",")
    return broken[0] + " " + broken[1] + " " + date
