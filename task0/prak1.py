a=[]
b=[]
i=0
m=0
mnum=0
k=0
import random
while i<30:
    a.append(random.randint(-100,100))
    if a[i]%2!=0:
        b.append(a[i])
        k=1
    i=i+1
m=max(a)
mnum=a.index(m)
print('rand:',a,'\nmax:',m,'\nномер:',mnum)
if k==0:
    print('немає непарних чисел')
else:
    print('непарний список:',b,'\nсортирований список:',sorted(b,reverse=True))
