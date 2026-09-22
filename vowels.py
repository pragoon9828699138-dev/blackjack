a=input("")
a=a.lower()
b=len(a)-1
c=0
d=0
while c<=b:
    if a[c]=="a" or a[c]=="e" or a[c]=="i" or a[c]=="o" or a[c]=="u":
        d+=1
        c+=1
    else:
        c+=1
print(d)

