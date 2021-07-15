def greet(name, owner):
    answer = 'Hello guest'
    if name == owner:
        answer = 'Hello boss'
    return answer
