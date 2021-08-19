def owned_cat_and_dog(cat_years, dog_years):
    cat = cat_years
    dog = dog_years
    count_cat = 1
    count_dog = 1
    if cat > 24:
        while cat > 24:
            cat -= 4
            count_cat += 1
        human_cat = cat / 24 + count_cat
    elif cat == 24:
        human_cat = 2
    elif cat < 24 and cat >= 15:
        human_cat = 1
    else:
        human_cat = 0
    if dog > 24:
        while dog > 24:
            dog -= 5
            count_dog += 1
        human_dog = dog / 24 + count_dog
    elif dog == 24:
        human_dog = 2
    elif dog < 24 and dog >= 15:
        human_dog = 1
    else:
        human_dog = 0
    return [int(human_cat), int(human_dog)]
