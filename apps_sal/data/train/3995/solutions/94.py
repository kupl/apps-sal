def dating_range(age):
    return f"{int(age-0.10 * age)}-{int(age+0.10*age)}" if age < 14 else f"{int(age / 2 + 7)}-{int((age-7)*2)}"
