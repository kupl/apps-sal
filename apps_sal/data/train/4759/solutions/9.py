def to_acronym(input):
    
# =============================================================================
#     This function takes a string and make an acronym of it.
#     
#     Rule of making acronym in this kata:
#         split string to words by space char
#         take every first letter from word in given string
#         uppercase it
#         join them toghether
#     Eg:
#         Code wars -> C, w -> C W -> CW
# =============================================================================

    words = input.split()
    
    acronym = ""
    
    for word in words:
        acronym = acronym + word[0].upper()
        
    return acronym
