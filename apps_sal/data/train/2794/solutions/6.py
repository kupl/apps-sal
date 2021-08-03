def calculate_age(dob, now):
    return f"You will be born in {dob-now} {'years'if dob-now>1 else 'year'}." if dob > now else "You were born this very year!" if dob == now else f"You are {now-dob} {'years'if now-dob>1 else 'year'} old."
