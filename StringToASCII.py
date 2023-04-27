def string_to_ascii(s):
    """
    Converts a string to a list of ascii values.

    Args: 
        s: The string to convert.

    Returns:
        A list of corresponding ascii values.
    """
    ascii_vals = []
    for char in s:
        ascii_vals.append(ord(char))
    return ascii_vals