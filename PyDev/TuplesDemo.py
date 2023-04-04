d={1:'a',2:'c',3:'b',0:'a'}
x=sorted(d.items())
#print(x)
#print(type(x))
#print(dir(x))
for k,v in sorted(d.items()):
    print(k,":",v)
tmp=list()
for k,v in d.items():
    tmp.append((v,k))
print(tmp)
tmp=sorted(tmp,reverse=True)
print(tmp)
for v,k in tmp[:10]:
    print(k,v)

