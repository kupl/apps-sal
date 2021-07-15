def bumps(road):
    '''(string)-> string
    A string representation of the road will be the input.
    Tests will be made to ensure that there are less than 15
    bumps in the road.'''
    num_bumps = road.count('n')
    if num_bumps > 15:
        return 'Car Dead'
    return 'Woohoo!'

