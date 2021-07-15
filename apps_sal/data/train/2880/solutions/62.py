def seven(m):
    # create a list out of m
    m_list = list(str(m))
    
    # check if input fits
    if not len(m_list) >= 2:
        final = m
        step = 0
    else:
    
        # set step and proceed calculation
        step = 0

        while len(m_list) >=2:
            step +=1
    
            if len(m_list) > 2:
                # take the last digit * 2 and substract it from the rest
                result = int("".join(m_list[0:(len(m_list)-1)])) - 2*int(m_list[-1])
    
                # make a new list out of result
                result_list = list(str(result))
    
                # check if finished
                if len(result_list) >=2:
                    m_list = result_list
                else:
                    m_list = result_list
                    final = int("".join(result_list))
            else:
                step -= 1
                final = int("".join(m_list))
                break
            
    # return desired result
    return (final, step)
