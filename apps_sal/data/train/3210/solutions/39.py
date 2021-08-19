from collections import Counter


def get_strings(city):
    counting = Counter(city.lower())  # makes sure everything is lowercase
    dict(counting)
    output = ''
    # print(counting.items())
    for key, value in counting.items():

        if len(key.strip()) > 0:  # checks for whitespace, (0 is returned if there is whitespace)
            output += key + ':' + ('*' * value) + ','  # formats the output according to the task description

    output = output[:-1]  # removes the last ','
    print(output)
    return output
