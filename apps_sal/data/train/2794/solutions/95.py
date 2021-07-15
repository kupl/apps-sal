def calculate_age(birthyear, target):
    if birthyear == target:
        return 'You were born this very year!'
    elif birthyear > target:
        return 'You will be born in {} year{}.'.format(birthyear - target, 's' * ((birthyear - target) > 1))
    else:
        return 'You are {} year{} old.'.format(target - birthyear, 's' * ((target - birthyear) > 1 ))
