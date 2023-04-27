# RSA-Encryption
Supplementary repository for paper on RSA Cryptosystems.

## Main Runnables
- AliceBobRSAExample.py: 
    - This code demonstrates how to encrypt and decrypt a message using the RSA algorithm. It imports several functions from other Python files, including rsa_encrypt and rsa_decrypt for encryption and decryption, string_to_ascii and ascii_to_string for converting messages between strings and ASCII codes. The code sets up Bob's RSA key and defines a message from Alice, converts it to numerical values, encrypts it using Bob's public key, decrypts it using Bob's private key, and converts it back to a string. The final output is the original message printed by Alice and the decrypted message printed by Bob.

- CommonModulus.py
    - This Python script demonstrates a hypothetical attack on a two-recipient RSA encryption scheme with a common modulus. It encrypts a message with two different public keys, which are then intercepted by an attacker. The attacker uses the Extended Euclidean Algorithm to compute a linear combination of the two keys that yields 1. This linear combination is then used to decrypt the message and obtain the original plaintext. The script imports functions from several Python modules to implement RSA encryption and decryption, modular exponentiation, string-to-ASCII conversion, and the Extended Euclidean Algorithm.

## Utility files 
- RSADecryption.py 
    - Decrypts a list of encrypted values using RSA decryption 
    with the given private key (d, n).
- RSAEncryption.py
    - Encrypts a list of values using RSA encryption with the 
    given public key (e, n).
- ExtendedEuclidean.py
    - Performs the Extended Euclidean Algorithm on two numbers.
    Finds GCD and the "Bezout" coefficients.
- ModularExponentiation.py
    - Computes b^e mod m using the modular exponentiation.
- ModularMultiplicativeInverseEEA.py
    - Finds the modular multiplicative inverse of a modulo m using the extended Euclidean algorithm.
- ASCIIToString.py
    - Converts a list of ascii values to a string.
- StringToASCII.py
    - Converts a string to a list of ascii values.