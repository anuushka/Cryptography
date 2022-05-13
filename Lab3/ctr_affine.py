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

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def getKey():
    while True:
        key1 = int(input('Enter the key(number): '))
        gcd, x, y = gcdExtended(key1, 256)
        if gcd == 1:
            key2 = x % 256
            return key1, key2

def affine(realText, step):
    outText = ''
    for eachLetter in realText:
        outText += chr((ord(eachLetter) * step) % 256)
    return outText

wrd = []
wrdt = []
Text = input("Enter plain text: ")
step = getKey()
print('Encrypt key: ', step[0])
print('Decrypt key: ', step[1])

Textbin = binArray(Text)
for i in range(len(Textbin)):
    print(Text[i] + ' ' + str(ord(Text[i])) + ' p' + str(i + 1), Textbin[i])

counter = 0
for p in Textbin:
    c = affine(str(counter), step[0])
    c = decimalToBinary(ord(c), 8)
    c = logical_xor(c, p)
    wrd.append((c))
    counter += 1

print('Plain text:', Textbin)
print('CBC text:', wrd)

counter = 0
for c in wrd:
    p = affine(str(counter), step[0])
    p = decimalToBinary(ord(p), 8)
    p = logical_xor(p, c)
    wrdt.append((p))
    counter += 1

print('CBC decrypt:', wrdt)