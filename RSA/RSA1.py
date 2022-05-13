from defs import *


def encrypt(me, e, n):
    c = powE(me,e,n)
    print("Encrypted Message is: ", c)
    return c

def decrypt(me, d, n):
    p = powE(me,d,n)
    print("Decrypted Message is: ", p)
    return p


message = int(input("Enter the message to be encrypted: ")) 

n, e, d = rand_e()

print("Public key: ({}, {})".format(e, n))
print("Private key: ({}, {})".format(d, n))
print("Original Message is: ", message)

c = encrypt(message, e, n)
p = decrypt(c, d, n)