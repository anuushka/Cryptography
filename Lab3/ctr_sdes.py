p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
p8 = [6, 3, 7, 4, 8, 5, 10, 9]

ip8 = [2, 6, 3, 1, 4, 8, 5, 7]
ep8 = [4, 1, 2, 3, 2, 3, 4, 1]
p4 = [2, 4, 3, 1]
ip_1 = [4, 1, 3, 5, 7, 2, 8, 6]

s0 = [['01', '00', '11', '10'],
      ['11', '10', '01', '00'],
      ['00', '10', '01', '11'],
      ['11', '01', '11', '10']]

s1 = [['00', '01', '10', '11'],
      ['10', '00', '01', '11'],
      ['11', '00', '01', '00'],
      ['10', '01', '00', '11']]


def ip(kk, st):
    s = ''
    for i in kk:
        s = s + st[i - 1]
    return s

def dev5(key10, b):
    key5L = key10[0:5]
    key5R = key10[5:]
    key5L = key5L[b:] + key5L[0:b]
    key5R = key5R[b:] + key5R[0:b]
    key10 = key5L + key5R
    k1 = ip(p8, key10)
    return k1, key10

def key(key10):
    key10 = ip(p10, key10)
    k1, key10 = dev5(key10, 1)
    k2, key10 = dev5(key10, 2)
    return k1, k2

def decimalToBinary(n, b):
    bnr = bin(n).replace("0b", "")
    x = bnr[::-1]  # this reverses an array.
    while len(x) < b:
        x += '0'
    bnr = x[::-1]
    return bnr

def binArray(text):
    binArr = []
    for i in text:
        p = decimalToBinary(ord(i), 8)
        binArr.append(p)
    return binArr

def logical_xor(str1, str2):
    xr = ''
    for i in range(0, len(str1)):
        b = '1'
        if str1[i] == str2[i]:
            b = '0'
        xr = xr + b
    return xr


def RC(str):
    s = 0
    if str == '01':
        s = 1
    if str == '10':
        s = 2
    if str == '11':
        s = 3
    return s

def rund(P, k):
    L = P[0:4]
    R = P[4:]
    ep = ip(ep8, R)
    ep = logical_xor(ep, k)

    s0r = RC(ep[0] + ep[3])
    s0c = RC(ep[1] + ep[2])
    s1r = RC(ep[4] + ep[7])
    s1c = RC(ep[5] + ep[6])

    P4 = s0[s0r][s0c]
    P4 += s1[s1r][s1c]

    P4 = ip(p4, P4)
    P4 = logical_xor(P4, L)
    P = R + P4
    return P


def EN(K, P):
    k1 = K[0]
    k2 = K[1]

    P = ip(ip8, P)
    P = rund(P, k1)
    P = rund(P, k2)
    P = P[4:] + P[0:4]
    P = ip(ip_1, P)
    return P


def DE(K, P):
    k = []
    k.append(K[1])
    k.append(K[0])
    return EN(k, P)

def findKey(P, C):
    for i in range(633, 645):
        ky = decimalToBinary(i, 10)
        tkr1 = key(ky)
        print(i, ky, EN(tkr1, P), DE(tkr1, C))


def checkKey(P, key1, key2):
    key1 = '1010000010'
    key2 = '1010000011'
    k1 = key(key1)
    k2 = key(key2)
    print(P)
    C = EN(EN(P, k1), k2)
    P1 = DE(DE(C, k2), k1)
    print(C)


key10 = '0111111101'

K = key(key10)
print(K)

wrd = []
wrdt = []

Text = "CCC One Nine Two"
Textbin = binArray(Text)
#Textbin = ['00000001', '00000010', '00000100']
for i in range(len(Textbin)):
    print(Text[i] + ' ' + str(ord(Text[i])) + ' p' + str(i + 1), Textbin[i])

counter = 0
for p in Textbin:
    count = decimalToBinary(counter, 8)
    c = EN(K, count)
    c = logical_xor(c, p)
    wrd.append((c))
    counter += 1

print('plain text:', Textbin)
print('CBC text:', wrd)

counter = 0
for c in wrd:
    count = decimalToBinary(counter, 8)
    p = EN(K, count)
    p = logical_xor(c, p)
    wrdt.append((p))
    counter += 1
print('CBC decrypt:', wrdt)
