def str_count(strng, letter):
    quantity_letter = 0
    for i in strng:
        if i == letter:
            quantity_letter = quantity_letter + 1
    return quantity_letter
