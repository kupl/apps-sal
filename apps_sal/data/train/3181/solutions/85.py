def check_alive(health):
    if health <= 0:
        return health != health
    else:
        return health == health
