def subcuboids(Q, W, E):
    return Q * -~Q * W * -~W * E * -~E >> 3
