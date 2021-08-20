def michael_pays(costs):
    micheal = 0
    if costs < 5:
        micheal = costs
    elif 1 / 3 * costs > 10:
        micheal = costs - 10
    else:
        micheal = costs - 1 / 3 * costs
    try:
        if isinstance(micheal, float):
            micheal = float('{0:.2f}'.format(micheal))
    except:
        micheal = micheal
    return micheal
