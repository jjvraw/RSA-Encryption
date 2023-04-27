def mod_exp(b, e, m):
    """
    Computes b^e mod m using the modular exponentiation.

    Args:
        b: The base.
        e: The exponent.
        m: The modulus.

    Returns:
        A list of tuples (e ,b ,r) which represents
        each row entry of an exponentiation table.

    """
    result = 1
    values = []
    values.append((e, b, result))
    while e > 0:
        if e % 2 == 1:
            result = (result * b) % m
        e = e >> 1
        b = (b * b) % m
        values.append((e, b, result))
    return result, values

