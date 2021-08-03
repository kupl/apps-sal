def check_alive2(func):
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        return result
    return wrapper


@check_alive2
def check_alive(health):
    return True if health >= 1 else False
