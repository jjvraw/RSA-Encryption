def ascii_to_string(ascii_vals):
    """
    Converts a list of ascii values to a string.

    Args: 
        ascii_vals: The list of ascii values 
                    to convert.

    Returns:
        The corresponding string.
    """
    s = ""
    for val in ascii_vals:
        s += chr(val)
    return s