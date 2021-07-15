def over_the_road(address, n):
    # Loops, dictionaries and maps didn't meet performance requirements. Now trying pure math
    return (n * 2) - address + 1

    #all_addr = {index: value for index, value in enumerate(range((n*2)+1,-1,-1))}
    #rev_all_addr = {}
    #count = n * 2
    
    # return [value for index, value in enumerate(range((n*2)+1,-1,-1)) if index == address][0]
    # even_addr = n * 2
    
    # map opposite addresses
#     for odd_addr in range(1, even_addr):
#         if odd_addr % 2 > 0:
#             all_addr[odd_addr] = even_addr
#             even_addr -= 2
#     for i in range(1, count):
#         all_addr[i] = count
#         count -= 1
    
    # invert address
    # rev_all_addr = {even_addr: odd_addr for odd_addr, even_addr in all_addr.items()}
    #return all_addr[address]


#     if address % 2 > 0:
#         return all_addr[address]
#     else:
#         return rev_all_addr[address]
        #return [odd_addr for odd_addr, even_addr in all_addr.items() if even_addr == address][0]

