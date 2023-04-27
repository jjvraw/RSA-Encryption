from RSAEncryption import rsa_encrypt
from StringToASCII import string_to_ascii
from ASCIIToString import ascii_to_string
from ExtendedEuclidean import extended_euclidean_algorithm
from ModularExponentiation import mod_exp

# Alice wishes to send the following message:
m_allice = "COMMON MODULUS"
ascii_m_allice =  string_to_ascii(m_allice)

# Alice receives the following from two recipients:
e1 = 191
e2 = -133
n = 31 * 37

# Alice encryptes the message using the first recipient's public key:
c1 = rsa_encrypt(ascii_m_allice, e1, n)

# Alice encryptes the message using the second recipient's public key:
c2 = rsa_encrypt(ascii_m_allice, e2, n)

# An attacker intercepts the keys (e1, n), (e2,n) & c1 and c2
# The attacker computes x and y using the Extended Euclidean Algorithm
# such that x * e1 + y * e2 = 1
eea_rows = extended_euclidean_algorithm(e2, e1)
x = eea_rows[-1][2]
y = eea_rows[-1][3]

# The attacker uses the following formula to compute the message:
ascii_m_attacker = []
for i in range(len(c1)):
    mi = (mod_exp(c1[i], y, n)[0] * mod_exp(c2[i], x, n)[0]) % n
    ascii_m_attacker.append(mi)

# The attacker decrypts the message:
m_attacker = ascii_to_string(ascii_m_attacker)

print(m_attacker)