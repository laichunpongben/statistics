import scipy.special as spec

def pmf(n,p,t,x):
    return -(1 - (1-p)**(n-x) * p**x * spec.binom(n,x) * spec.hyp2f1(1,-n+x,1+x,p/(p-1)))**t + \
    (1 - (1-p)**(-1+n-x) * p**(1+x) * spec.binom(n,1+x) * spec.hyp2f1(1,1-n+x,2+x,p/(p-1)))**t

def mean(n,p,t):
    s = 0
    for x in range(0,n+1):
        s += x * pmf(n,p,t,x)
    return s

n,p,t=100,1/6,6
print(mean(n,p,t))
