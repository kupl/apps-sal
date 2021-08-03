def london_city_hacker(journey):
    vehicle = "".join("t" if isinstance(j, str) else "b" for j in journey).replace("bb", "b")
    return f"£{sum(2.4 if v == 't' else 1.5 for v in vehicle):.2f}"
