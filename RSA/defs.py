import math
import random
from datetime import datetime

#-------start----------------------ANSI_X9_17 with EDE(Triple sdes)------------------------------#
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

def DT():
    now = datetime.now()
    dtnew = str(now)[-1:]
    p = decimalToBinary(ord(dtnew), 8)
    return p

def EDE(K, P):
    return EN(K[0], DE(K[1], EN(K[0], P)))

def ANSI_X9_17(K, vi):
    P = DT()
    ede1 = EDE(K, P)
    vi = logical_xor(vi, ede1)
    RI = EDE(K, vi)
    vi = logical_xor(RI, ede1)
    vi = EDE(K, vi)
    return  RI, vi

#-------finish----------------------ANSI_X9_17 with EDE(Triple sdes)------------------------------#

def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)           
    return roots

def primefactors(n):
    pf=[]
    #тэгш тоо байвал
    r=0
    while n % 2 == 0:
        r+=1
        n //=2
    if r!=0:
        pf.append([2,r])
    #n сондгой тоо болсон
    for i in range(3,int(math.sqrt(n))+1,2):
        r=0
        while (n % i == 0):
            r+=1
            n //=i
        if r!=0:
            pf.append([i,r])
    if n > 2:
        pf.append([n,1])
    return pf

def miller_rabin(n):
    if n == 1:
        return True
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n != 7 and n % 7 == 0:
        return False
    k, q = 0, n - 1
    while q % 2 == 0:
        k += 1
        q //= 2
    a = random.randrange(2, n - 1)
    x = pow(a, q, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(k - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False

def EulerFunction(N):
    '''if miller_rabin(N[0]):
    return (N[0]-1)*N[0]**(N[1]-1)'''
    if miller_rabin(N)== True:
        return N-1
    else:
        X = primefactors(N)
        if len(X) == 2:
            return (X[0][0]-1)*X[0][0]**(X[0][1]-1) * (X[1][0]-1)*X[1][0]**(X[1][1]-1)
        else:
            return (X[0][0]-1)*X[0][0]**(X[0][1]-1)

def powE(a,b,n):
    b = bin(b).replace("0b","")
    c,f = 0,1
    for i in b:
        c = c*2
        f = (f*f) % n
        if i == '1':
            c = c + 1
            f = (f*a) % n
    return f

def rand_e():
    p, q = pqrand()
    n = p * q
    flag = EulerFunction(n)
    e = random.randrange(1,flag)
    a = True
    e = e + 1
    while a:
        gcd, x, y = gcdExtended(e, flag)
        if gcd == 1:
            return n, e, x%flag
        e += 1

def find_d(n, e):
    pn  = EulerFunction(n)
    f = True
    i = 2
    while f == True:
        if e * i % pn == 1:  
            return i 
        i += 1

def rnd_prime():
    pr = [10000011, 10001001, 10001011, 10010101, 10010111, 
    10011101, 10100011, 10100111, 10101101, 10110011, 
    10110101, 10111111, 11000001, 11000101, 11000111, 
    11010011, 11011111, 11100011, 11100101, 11101001, 
    11101111, 11110001, 11111011, 100000001, 100000111, 
    100001101, 100001111, 100010101, 100011001, 100011011, 
    100100101, 100110011, 100110111, 100111001, 100111101]
    return pr

def pqrand():
    pr = rnd_prime()
    vi = '00000000'

    key1 = '1001111100'
    key2 = '1010000010'
    k1 = key(key1)
    k2 = key(key2)
    K = [k1, k2]
    rnd1, vi = ANSI_X9_17(K, vi)
    rnd2, vi = ANSI_X9_17(K, vi)
    p = pr[int(rnd1, 10) % len(pr)]
    q = pr[int(rnd2, 10) % len(pr)]
    p = binaryToDecimal(p)
    q = binaryToDecimal(q)

    return p, q

def toBinary(a):
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        b = int(bin(i)[2:])
        if len(str(b)) < 8 and len(str(b)) > 6:
            b = '0' + str(b)
        elif len(str(b)) < 7 and len(str(b)) > 5:
            b = '00' + str(b)
        m.append(b)
    return m

def to8Digit(ms):
    arr = []
    a = ''
    c = 0
    for i in ms:
        a += i
        c += 1
        if c == 8:
            arr.append(a)
            c = 0
            a = ''
    return arr

def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal 