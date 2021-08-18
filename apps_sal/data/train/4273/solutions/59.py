def shorten_to_date(long_date):
    jour, mois, year = (long_date.split())[0], (long_date.split())[1], (long_date.split())[2]
    if year[1] == ",":
        year = year[0]
    elif year[2] == ",":
        year = year[0] + year[1]
    date = jour + " " + mois + " " + year
    return date
