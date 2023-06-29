f=open("17_6024.txt")
a=[]
for s in f:
    a.append(int(s))
nn=[]
for x in a:
    if x%100==12:
        nn.append(x)
m=max(nn)
p=[]
for i in range(len(a)-1):
    # if (((a[i]%100==12)+(a[i+1]%100==12))==1) and ((a[i]+a[i+1])**2<m**2):
    if ((a[i] % 100 == 12 and a[i+1] % 100 != 12) or (a[i+1] % 100 == 12 and a[i] % 100 != 12)) and ((a[i]+a[i+1])**2<m**2):
        p.append(a[i]+a[i+1])
print(len(p))