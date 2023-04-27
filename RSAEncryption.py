from typing import List

def rsa_encrypt(values: List[int], e: int, n: int) -> List[int]:
    """
    Encrypts a list of values using RSA encryption with the 
    given public key (e, n).
    
    Args:
        values: A list of integers to be encrypted.
        e: The public key exponent.
        n: The public key modulus.
        
    Returns:
        A list of integers representing the encrypted values.
    """
    encrypted_values = []
    for val in values:
        encrypted_val = pow(val, e, n)
        encrypted_values.append(encrypted_val)
    return encrypted_values