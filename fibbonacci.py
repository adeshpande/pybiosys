

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

if __name__=="__main__":
    n = F(7)
    print n
