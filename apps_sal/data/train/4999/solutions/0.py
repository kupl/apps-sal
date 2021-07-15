def capital(capitals):
    return [f"The capital of {c.get('state') or c['country']} is {c['capital']}" for c in capitals]
