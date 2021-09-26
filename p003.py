import eulerlib

def function():
    n = 600851475143
    while True:
        p = smallestPrimeFactor(n)
        if (p < n):
            n //= p
        else:
            return str(n)
    
def smallestPrimeFactor(n):
    assert n >=2
    for i in range(2, eulerlib.sqrt(n) + 1):
        if n % i == 0:
            return i
    return n

if __name__ == "__main__":
    print(function())