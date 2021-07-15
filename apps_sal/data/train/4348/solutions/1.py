def calc_fuel(n):
    time = n * 11
    lava, blaze = divmod(time, 800)
    blaze, coal = divmod(blaze, 120)
    coal, wood = divmod(coal, 80)
    wood, stick = divmod(wood, 15)
    
    return {'lava': lava, 'blaze rod': blaze, 'coal': coal, 'wood': wood, 'stick': stick}

