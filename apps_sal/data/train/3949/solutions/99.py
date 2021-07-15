def calculate_tip(amount: int, rating: str) -> int:
    return {
        "Terrible": round((lambda x: x * 0.00)(amount) + 0.5),
        "Poor": round((lambda x: x * 0.05)(amount) + 0.5),
        "Good": round((lambda x: x * 0.10)(amount) + 0.5),
        "Great": round((lambda x: x * 0.15)(amount) + 0.5),
        "Excellent": round((lambda x: x * 0.20)(amount) + 0.5),
    }.get(rating.title(), "Rating not recognised")
