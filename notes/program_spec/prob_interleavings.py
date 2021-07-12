import math

def f(n, p):
    return math.factorial(n*p) / (math.factorial(n)**p)

def g(n, p):
    return max(1000 * n**2, 1)
    #return (100 * n)**(2*p)
    #return math.floor( f(n,p) / 2 )
    #rv = math.floor( f(n,p) / max(n**8,1) )
    #rv = 1.18e29
    #rv = 5.7e28
    #rv = 1e27
    #return max( rv, 10 )

C = 1e-6

def num_bad_states(i, j, p):
    # which to use, i or j?
    return max(f(i,p) * C, 1)

def h(i, j, p):
    #return f(j-i,p) / f(j,p)
    return num_bad_states(i,j,p) * f(j-i,p) / f(j,p)

def always_random(i, j, p):
    prob = 1.0
    for k in range(i, j+1):
        #prob *= (1 - h(i, i+k, p))**g(i+k,p)
        prob *= (1 - h(i, k, p))**g(k,p)
    return 1-prob

def diff_path_per_k(i, j, p):
    prob = 1.0
    for k in range(i, j+1):
        prob *= 1 - min(h(i, i+k, p)*g(i+k,p), 1)
    return 1-prob

for i in range(0,51,10):
    j = i + 5
    p = 2
    r = always_random(i, j, p)
    s = diff_path_per_k(i, j, p)
    print("rand={:.5f}, diff={:.5f} | f(i,p)={:e}, g(i,p)={:e}, i={}, j={}".format(r,s,f(i,p),g(i,p),i,j))

#print(f(0, 20))
