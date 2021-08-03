def michael_pays(costs):
    if costs < 5:
        return round(costs, 2)
    else:
        return round(max(costs - 10, 2 / 3 * costs), 2)
