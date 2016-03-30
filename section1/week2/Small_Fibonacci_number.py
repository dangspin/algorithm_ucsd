# python2

def Fib_iter(n):
    """
    This is the iterative version of Fibonacci number. In order to accelrate the speed of the code,
    here we apply the for loop instead of recursion
    """
    order=int(n)
    if n<=1:
        return order
    else:
        fib_list=[0]*(order+1)
        fib_list[0]=0
        fib_list[1]=1
        for i in range(2,order+1):
            fib_list[i]=fib_list[i-1]+fib_list[i-2]
        return fib_list[-1]

if __name__ == '__main__':
    n = int(raw_input())
    print Fib_iter(n)
