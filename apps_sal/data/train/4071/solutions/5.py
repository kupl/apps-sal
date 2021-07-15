def next_happy_year(year):
    while True:
        year+=1
        if len(set(c for c in str(year))) == len(str(year)):
            return year
