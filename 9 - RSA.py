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

print(f"Prime Number 1: {P}")
print(f"Prime Number 2: {Q}")
print(f"RSA Public Key: {E}")
print(f"Plain Text: {M}")

print()


# Calculating Modulo N
N = P*Q

# Calculating the Cipher Text
C = pow(M, E) % N


print(f"The Cipher text is: {C}")
