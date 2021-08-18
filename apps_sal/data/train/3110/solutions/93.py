def two_decimal_places(num):
    try:
        return round(num + 0.0001, 2)
    except (TypeError):
        return 0
