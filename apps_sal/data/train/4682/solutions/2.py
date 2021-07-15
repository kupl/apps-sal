from datetime import date, timedelta
get_date = __import__("re").compile(r"(\d\d)\.(\d\d)\.(\d\d\d\d)").search

def date_correct(my_date):
    if not my_date: return my_date
    try: d, m, y = map(int, get_date(my_date).groups())
    except AttributeError: return
    return (date(y+(m-1)//12, (m-1)%12+1, 1) + timedelta(d-1)).strftime("%d.%m.%Y")
