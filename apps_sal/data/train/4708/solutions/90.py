def human_years_cat_years_dog_years(human):
    def animal(h, p):
        r = 0
        for i in range(1, h + 1):
            if i == 1:
                r += 15
            elif i == 2:
                r += 9
            else:
                r += p
        return r

    return [human, animal(human, 4), animal(human, 5)]
