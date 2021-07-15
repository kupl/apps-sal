def calculate_tip(amount, rating):
    dict = {"terrible": 0,
    "poor": 5,
    "good": 10,
    "great": 15,
    "excellent": 20}
    try:
        result = float(amount) / float(100) * dict[rating.lower()]
        if result != int(str(result).split(".")[0]):
            return int(str(result).split(".")[0]) + 1
        return int(result)
    except KeyError:
        return 'Rating not recognised'
