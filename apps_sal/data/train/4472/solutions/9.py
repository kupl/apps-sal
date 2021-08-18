def bear_fur(bears):
    for i in range(len(bears) - 1):
        if bears[i] == 'black' and bears[i + 1] == 'black':
            return 'black'
        elif bears[i] == 'white' and bears[i + 1] == 'white':
            return 'white'
        elif bears[i] == 'brown' and bears[i + 1] == 'brown':
            return 'brown'
        elif bears[i] == 'black' and bears[i + 1] == 'white':
            return 'grey'
        elif bears[i] == 'black' and bears[i + 1] == 'brown':
            return 'dark brown'
        elif bears[i] == 'white' and bears[i + 1] == 'black':
            return 'grey'
        elif bears[i] == 'white' and bears[i + 1] == 'brown':
            return 'light brown'
        elif bears[i] == 'brown' and bears[i + 1] == 'black':
            return 'dark brown'
        elif bears[i] == 'brown' and bears[i + 1] == 'white':
            return 'light brown'
        else:
            return 'unknown'
