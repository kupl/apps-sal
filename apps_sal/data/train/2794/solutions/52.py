def calculate_age(year_of_birth, current_year):
    gap = current_year - year_of_birth
    if gap > 0: return "You are {} year{} old.".format(gap, 's' if gap>1 else '')
    if gap < 0: return "You will be born in {} year{}.".format(-gap, 's' if gap<-1 else '')
    return "You were born this very year!"

