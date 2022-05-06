"""

The 8 bit input plain text is: **01110010**, Put the plain text into IP-8(initial
permutation) table, then perform Expansion and Permutation on right half. Use the
following TWO round keys K1 and K2 respectively and perform the XOR operation<br>
K1: 1 0 1 0 0 1 0 0
K2: 0 1 0 0 0 0 1 1
Show the result after second round.

"""


def PC(ip, pc):
    result = ""
    for i in pc:
        result += ip[i-1]

    return result


def XOR(a, b):
    res = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            res += "0"
        else:
            res += "1"
    return res


def apply_sbox(s, data):
    row = int("0b" + data[0] + data[-1], 2)
    col = int("0b" + data[1:3], 2)
    return bin(s[row][col])[2:]


def swapFunction(expansion, s0, s1, key, message):
    P4table = [2, 4, 3, 1]
    left = message[:4]
    right = message[4:]
    temp = PC(right, expansion)
    # print(f"{temp[:4]} {temp[4:]}")
    temp = XOR(temp, key)
    l = apply_sbox(s0, temp[:4])
    r = apply_sbox(s1, temp[4:])
    l = "0" * (2 - len(l)) + l
    r = "0" * (2 - len(r)) + r
    temp = PC(l + r, P4table)
    temp = XOR(left, temp)
    return temp + right


if __name__ == '__main__':

    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    plainText = "01110010"
    K1 = "10100100"
    K2 = "01000011"
    expansion = [4, 1, 2, 3, 2, 3, 4, 1]
    s0Box = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    s1Box = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    temp = PC(plainText, IP)
    # print(f"{temp[:4]} {temp[4:]}")
    temp = swapFunction(expansion, s0Box, s1Box, K1, temp)
    temp = temp[4:] + temp[:4]
    temp = swapFunction(expansion, s0Box, s1Box, K2, temp)
    CT = PC(temp, IP_inv)
    print("Cipher text is:", CT)
