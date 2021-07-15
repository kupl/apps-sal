def calculate_age(year_of_birth, current_year):
    ad = current_year - year_of_birth    # Age Difference
    sfx = 's'*(abs(ad)>1)                # Suffix
    return "You were born this very year!" if ad is 0 else f"You will be born in {abs(ad)} year{sfx}." if ad < 0 else f"You are {ad} year{sfx} old."

