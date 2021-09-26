import math 

def f():
    n = 100
    factorial = math.factorial(n)
    string = str(factorial)
    ans = sum(int(c) for c in string)
    return ans

if __name__ == "__main__":
    print(f())