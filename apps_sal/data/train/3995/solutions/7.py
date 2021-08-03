def dating_range(age):
    return f"{age // 2 + 7}-{2 * age - 14}" if age > 14 else f"{age * 9 // 10}-{age * 11 // 10}"
