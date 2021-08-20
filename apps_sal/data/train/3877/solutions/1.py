CHR_TO_NUM = str.maketrans('abcdefghijklmnopqrstuvwxyz', '22233344455566677778889999')
NUM_TO_CHR = str.maketrans('23456789', 'adgjmptw')


def T9(words, seq):
    return [word for word in words if word.lower().translate(CHR_TO_NUM) == seq] or [seq.translate(NUM_TO_CHR)]
