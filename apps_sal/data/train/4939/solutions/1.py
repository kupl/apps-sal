def coffee_limits(year, month, day):
    health = int(f"{year:04d}{month:02d}{day:02d}")
    drinks = (int(d, 16) for d in ("cafe", "decaf"))
    return [next((cup for cup in range(1, 5001) if "dead" in f"{health + drink*cup:x}"), 0) for drink in drinks]

