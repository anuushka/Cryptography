import math
import random

def miller_rabbin(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
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

def euler_function(N):
    # if miller_rabbin(N[0]):
    return (N[0] - 1) * N[0] ** (N[1] - 1)

def primefactors(n):
    pf = []
    r = 0
    while n % 2 == 0:
        r += 1
        n = n // 2
    if r != 0:
        pf.append([2, r])

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        r = 0
        while (n % i == 0):
            r += 1
            n = n // i
        if r != 0:
            pf.append([i, r])
    if n > 2:
        pf.append([n, 1])
    return pf

def removeX(ef_list, a):
    for x in ef_list:
        if x % a == 0:
            ef_list.remove(x)

def eulertotient(n):
    ef_list = list(range(1, n + 1))
    ef_factorized = primefactors(n)
    for i in ef_factorized:
        removeX(ef_list, i[0])
    return ef_list
n = int(input("Please input number : "))
l = []
   
print(n,"is prime number :",miller_rabbin(n))
print("Prime factor of",n,"is :",primefactors(n))
print("Euler's totient number sequence: " ,len(eulertotient(n)))
print("Euler totient :",eulertotient(n))
