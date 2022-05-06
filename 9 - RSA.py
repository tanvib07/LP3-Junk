"""

Implement the RSA algorithm to generate the Cipher text.
Assume following details.
Two prime number p=11, q=7,
RSA Public Key=37,
Plaintext= 15

"""

P = 11  # Prime Number 1
Q = 7  # Prime Number 2
E = 37  # Public Key
M = 15  # Plain Text

# Calculating Modulo N
N = P*Q

# Calculating Cipher Text
C = pow(M, E) % N


print(C)
