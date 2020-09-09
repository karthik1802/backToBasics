# GCD Using Euclidean Algorithm

def gcd(a,b):
    if a == 0:
        return b
    else:
        if a>b:
            return gcd(a%b, b)
        else:
            return gcd(b%a, a)


print(gcd(12,4))