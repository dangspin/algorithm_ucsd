# Uses python2
import sys

def gcd(a, b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

def lcm(a, b):
    """
    This function calculate the least common multiple, we first calculate GCD, 
    and then use the relation LCM*GCD=a*b
    """
    return int((a*b)/gcd(a,b))

if __name__ == "__main__":
    a, b = map(int, raw_input().split())
    print(lcm(a, b))
