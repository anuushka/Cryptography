from defs import *

def encrypt_decrypt(me, k, n):
    m = powE(me,k,n)
    return m

def four_dig(mes):
    l = []
    s = ''
    for i in mes:
        ind = dic.index(i) + 1
        if len(str(ind)) < 2:
            ind = str(ind) + '0'
            ind = ind[::-1]
        s += str(ind)
        if len(s) == 4:
            l.append(int(s))
            s = ''
    if len(s) == 2:
        t = '00'
        s = t + s
        l.append(int(s))
    return l

def two_dig(lst):
    mes = ""
    for i in lst:
        if len(str(i)) == 4:
            mes += dic[int(str(i)[:2]) - 1]
            mes += dic[int(str(i)[2:]) - 1]
        elif len(str(i)) == 3:
            mes += dic[int(str(i)[:1]) - 1]
            mes += dic[int(str(i)[1:]) - 1]
        else:
            mes += dic[i - 1]
    return mes

def enc_list(lst):
    enclist = []
    for i in lst:
        enclist.append(encrypt_decrypt(i, e, n))
    return enclist

def dec_list(lst):
    enclist = []
    for i in lst:
        enclist.append(encrypt_decrypt(i, d, n))
    return enclist

dic = "abcdefghijklmnopqrstuvwxyz"
dic += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dic += "0123456789"
dic += "_-?<>[]()/:., "

message1 = input("Enter your message: ")
n, e, d = rand_e()
origlist1 = four_dig(message1)
encryptlist = enc_list(origlist1)
origlist2 = dec_list(encryptlist)
message2 = two_dig(origlist2)


print("----------------------------------")
print("Public key: ({}, {})".format(e, n))
print("Private key: ({}, {})".format(d, n))
print("----------------------------------")
print("Original Plan text: ", message1)
print("Original decimal is: ", origlist1)
print("Encrypted decimal is: ", encryptlist)
print("Decrypted decimal is: ", origlist2)
print("Decrypted Plan text: ", message2)





