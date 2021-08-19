def user_contacts(data):
    return {contact[0]: contact[1] if len(contact) > 1 else None for contact in data}
