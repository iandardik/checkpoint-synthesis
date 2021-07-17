import math

def choose(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def f(n, p):
    return math.factorial(n*p) / (math.factorial(n)**p)

def orig(p, i, k):
    return f(i,p) * f(k-i,p) / f(k,p)

def simpl(p, i, k):
    #j = i+k
    #return choose(i,k)**p / choose(p*j,p*k)
    return choose(k,i)**p / choose(k*p,i*p)

print(orig(2, 5, 5))
print(simpl(2, 5, 5))
