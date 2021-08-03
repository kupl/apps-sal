def calculate_age(year_of_birth, current_year):
    ans = current_year - year_of_birth
    if ans == 0:
        ans = "You were born this very year!"
    elif ans == 1:
        ans = "You are 1 year old."
    elif ans < 1 and ans != -1:
        ans = "You will be born in " + str(ans * -1) + " years."
    elif ans == -1:
        ans = "You will be born in 1 year."
    else:
        ans = "You are " + str(ans) + " years old."
    return ans
