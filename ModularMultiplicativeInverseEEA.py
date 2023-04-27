def modular_multiplicative_inverse(phi, d):
    """
    Finds the modular multiplicative inverse of a modulo m using the 
    extended Euclidean algorithm.

    Args:
        phi: The phi value.
        d: The d value to which the inverse is being found.

    Returns:
        A list of lists representing the rows of the extended euclidean 
        algorithm table.
    """
    extEuclidTable = []
    r = 1
    r0 = phi
    r1 = d
    x0 = 1
    y1 = 1
    x1 = 0
    y0 = 0
    q = 0

    extEuclidTable.append(["-", r0, x0, y0])
    extEuclidTable.append(["-", r1, x1, y0])

    while r != 0:
        q = r0 // r1
        r = r0 - q * r1
        x = x0 - q * x1
        y = y0 - q * y1
        r0 = r1
        r1 = r
        x0 = x1
        x1 = x
        y0 = y1
        y1 = y
        row = [q, r, x, y]
        extEuclidTable.append(row) # Add values to table

    return extEuclidTable