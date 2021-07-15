def michael_pays(costs):
    return round(costs - (costs >= 5)*min(costs/3., 10), 2)
