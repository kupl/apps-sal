def check_alive(health):
    if health >0 and health <=10:
        return True
    elif health <=0 and health >=(-10):
        return False
