from typing import List

def rsa_decrypt(encrypted_values: List[int], d: int, n: int) -> List[int]:
    """
    Decrypts a list of encrypted values using RSA decryption 
    with the given private key (d, n).
    
    Args:
        encrypted_values: A list of integers to be decrypted.
        d: The private key exponent.
        n: The public key modulus.
        
    Returns:
        A list of integers representing the decrypted values.
    """
    decrypted_values = []
    for encrypted_val in encrypted_values:
        decrypted_val = pow(encrypted_val, d, n)
        decrypted_values.append(decrypted_val)
    return decrypted_values
