f = open("17_8504.txt")
a = []
for i in f:
    a.append(int(i))
print(a)

b = []
for j in a:
    if j  >=  100 and j < 1000 and j % 10 == 5:
    # if 100 <= j <= 100 and j % 10 == 5:
        b.append(j)
print(b)
min = min(b)
print(min)

p = []
for k in range(len(a) - 1):
    if ((a[k] >= 100 and a[k] < 1000) or (a[k + 1] >= 100 and a[k + 1] < 1000)) and ((a[k] + a[k + 1]) % min == 0 ):
        p.append(a[k] + a[k+1])
print(len(p), max(p))









# f=open("17.3.txt")
# a=[]
# for s in f:
# a.append(int(s))
# kr7=[]
#
# for x in a:
# if x%7==0:
# kr7.append(x)
# maxx=max(kr7)
#
# cymm=[]
# for i in range(len(a)-2):
# if (a[i]%10==9 and a[i+1]%10!=9 and a[i+2]%10!=9) or\
# (a[i]%10!=9 and a[i+1]%10==9 and a[i+2]%10!=9) or (a[i]%10!=9 and a[i+1]%10!=9 and a[i+2]%10==9):
# if (a[i]+a[i+1]+a[i+2])<maxx:
# cymm.append(a[i]+a[i+1]+a[i+2])
# print(len(cymm),max(cymm))