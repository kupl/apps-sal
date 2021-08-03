def capital(capitals):
    return [f"The capital of {s.get('state') or s.get('country')} is {s.get('capital')}" for s in capitals]
