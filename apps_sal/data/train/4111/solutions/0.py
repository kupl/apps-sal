def sabb(stg, value, happiness):
    sabbatical = (value + happiness + sum(1 for c in stg if c in "sabbatical")) > 22
    return "Sabbatical! Boom!" if sabbatical else "Back to your desk, boy."
