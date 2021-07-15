def duty_free(price: int, discount: int, holiday_cost: int) -> int:
    return int(holiday_cost // ((discount / 100) * price))
