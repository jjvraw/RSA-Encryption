from RSAEncryption import rsa_encrypt
from RSADecryption import rsa_decrypt
from StringToASCII import string_to_ascii
from ASCIIToString import ascii_to_string

if __name__ == "__main__": 

    # Set up Bob's key
    p = 61
    q = 59
    n = p * q
    phin = (p-1) * (q-1)
    d = 953
    e = 1457

    # Alice defines a message
    alice_message = "MEET AT NINE"
    print("Alice's Message >>", alice_message)

    #Alice converts the message to numerical values
    ascii_list = string_to_ascii(alice_message)
    print("Alice's Message in ASCII >>", ascii_list)
    
    # Alice encrypts the message using Bob's public key (d,n)
    encrypted_message = rsa_encrypt(ascii_list, d, n)
    print("Alice's Encrypted Message >>", encrypted_message)

    # Bob decrypts the message using his private key (e,n)
    decrypted_message = rsa_decrypt(encrypted_message, e, n)
    print("Bob's Decrypted Message >>", decrypted_message)

    # Bob converts the numerical values back to a string
    bob_message = ascii_to_string(decrypted_message)
    print("Bob's Message >>", bob_message)

    