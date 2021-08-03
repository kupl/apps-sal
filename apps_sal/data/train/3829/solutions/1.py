def build_square(blocks):
    return (blocks.count(4)
    + min(blocks.count(3), blocks.count(1))
    + ((blocks.count(1) - min(blocks.count(3), blocks.count(1))) / 4)
        + (blocks.count(2) / 2)) >= 4
