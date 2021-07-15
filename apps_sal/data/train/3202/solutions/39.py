def greet(name, owner):
    return{
        owner : 'Hello boss'
    }.get(name, 'Hello guest')
