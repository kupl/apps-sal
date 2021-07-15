def numeric_formatter(template, digits = "1234567890"):
    counter = 0
    formatted = ""
    for char in template:
        if counter >= len(digits):
            counter = 0
        if char.isalpha():
            formatted += digits[counter]
            counter += 1
        else:
            formatted += char
    return formatted
