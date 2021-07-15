def coffee_limits(year, month, day):
    health = int(f"{year:04d}{month:02d}{day:02d}")
    limit = lambda drink: next((cup for cup in range(1, 5001) if "dead" in f"{health + drink*cup:x}"), 0)
    return [limit(int(drink, 16)) for drink in ("cafe", "decaf")]
