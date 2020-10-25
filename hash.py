"""
Python code for hashing function
"""
def search(x):
    if x>0:
        if has[x][0]==1:
            return True
#if X is negative take the absolute value of x.
    x=abs(x)
    if has[x][1]==1:
        return True
    return False

def insert(a,n):
    for i in range(0,n):
        if a[i]>=0:
            has[a[i]][0]=1
        else:
            has[abs(a[i])][1]=1

a=[-1,9,-5,-8,-5,-2]
n=len(a)

max=1000

has = [[0 for i in range(2)]
        for j in range(max+1)]
insert(a,n)

x=10
if search(x) is True:
    print('\nPresent\n')
else:
    print('\nNot present\n')