def encode(message):
    return message.translate(message.maketrans('GAgaDEdeRYryPOpoLUluKIki', 'AGagEDedYRyrOPopULulIKik'))


def decode(message):
    return message.translate(message.maketrans('GAgaDEdeRYryPOpoLUluKIki', 'AGagEDedYRyrOPopULulIKik'))
