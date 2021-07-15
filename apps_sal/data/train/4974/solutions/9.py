def user_contacts(data):
    return {d[0]:d[1] if len(d)>1 else None for d in data}
    # Your code here.

