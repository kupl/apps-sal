def michael_pays(cost):
    return round(cost if cost < 5 else max(cost * 2 / 3, cost - 10), 2)
