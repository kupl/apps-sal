def remove_rotten( bag_of_fruits ):
    return [ el.replace( "rotten", "" ).lower() for el in bag_of_fruits ] if bag_of_fruits else [ ]

