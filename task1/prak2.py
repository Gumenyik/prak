a=input()
l=len(a)
num=[]
num1=[]
slo=''
i=0
while i<l:
    a1=''
    b=a[i]
    while '0'<=b<='9':
        a1+=b
        i+=1
        if i <l:
            b=a[i]
        else:
            break
    i+=1
    if a1!='':
        num.append(int(a1))
        slo=slo+' '
    if b.isdigit()==False:
        slo=slo+b
print('масив чисел:',num,'\nрядок без чисел:',slo)
slo=slo.title()
slo2=''
q=''
for i in slo:
    if i==' ':
        q=q.upper()
    slo2+=q
    q=i
q=q.upper()
slo2+=q
print('рядок в якому кожне слово починається і закінчується великою літерою:',slo2)
print('максимальне значення в масиві чисел:',max(num))
for i in num:
    if i==max(num):
        num1.append(i)
    else:
        num1.append(i**num.index(i))
print('новий масив чисел:',num1)
        

