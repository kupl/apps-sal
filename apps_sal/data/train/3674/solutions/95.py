def add_binary(a, b):

    # =============================================================================
    #     This function adds two numbers together and returns their sum in binary.
    #     The conversion is done after the addition.
    #
    #     The functionn returns the binary number as a string.
    #
    #     Examples:
    #         add_binary(2,2) ==> "100"
    #         add_binary(51,12) ==> "111111"
    # =============================================================================

    return bin(a + b)[2::]
