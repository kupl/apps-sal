def find_missing_number(sequence):
    if not sequence:
        return 0
    elif not sequence.replace(" ", "").isdigit():
        return 1
    
    new_seq = list( map( int, sequence.split()))
    try :
        ans =  min( set( range( 1, max( new_seq) + 1)).difference( set( new_seq)))
        return ans
    except :
        return 0
