#searching
def search(p,t):
    m = len(p)
    n = len(t)
    if m>n:
        return -1
    else:
        for i in range(n-m+1):
            if p == t[i:i+m]:
                return i 
            if i==n-m:
                return -1
print(search('abc','aaddbcfdfsf'))