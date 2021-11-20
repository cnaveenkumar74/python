def armstrong(a):
    x = 0
    for i in range(len(a)):
        x += int(a[i])**len(a)
    return 1 if (x==int(a)) else 0

a= input()
if(armstrong(a)==0):
    print("Not armstrong")
else:
    print("Armstrong")
