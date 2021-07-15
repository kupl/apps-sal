def greet(name, owner):
    return 'Hello ' + ['boss', 'guest'][name != owner]
