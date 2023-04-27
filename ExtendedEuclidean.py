def extended_euclidean_algorithm(a, b):
    """
    Performs the Extended Euclidean Algorithm on two numbers.
    Finds GCD and the "Bezout" coefficients.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        list: A list of rows for the Extended 
              Euclidean Algorithm table.
    """
    rows = []
    r, r_prev = a, b
    s, s_prev = 1, 0
    t, t_prev = 0, 1
    rows.append(("-", a, 1, 0))
    rows.append(("-", b, 0, 1))

    while r_prev != 0:
        quotient = r // r_prev
        r, r_prev = r_prev, r - quotient * r_prev
        s, s_prev = s_prev, s - quotient * s_prev
        t, t_prev = t_prev, t - quotient * t_prev
        rows.append((quotient, r, s, t))

    return rows