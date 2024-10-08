def is_prime(n):
    if n<=1:
        return False 
    else:
        for d in range(2, n):
            if n%d==0:
                return False 
    return True

def STgcdr(a,b):
    if a<b:
        a,b =b,a 
    if b==0:
        s=1
        t=0
        return a, s, t
    gcd,s1,t1 = STgcdr(b, a%b)
    s = t1
    t = s1-t1*(a//b)
    return gcd,s,t
print('The module is imported')