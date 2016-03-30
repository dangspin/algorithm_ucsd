# python2
import sys

def gcd(a, b):
    """
    This is the recursive version of finding the greatest common divisor. 
    I implement the Euclidean algorithm, which is a powerful way to solve this problem.
    """
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

if __name__ == "__main__":
    a, b = map(int, raw_input().split())
    print(gcd(a, b))
