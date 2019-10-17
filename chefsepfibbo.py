for i in range(int(input())):
    n=int(input())
    l=[0,1]
    li=[]
    for j in range(n-2):
        l.append(l[j]+l[j+1])
    for j in range(n):
        if(l[j]>=10):
            li.append(l[j]%10)
        else:
            li.append(l[j])
        
    l=[]
    l=li.copy()
    n=len(l)
    lii=[]
    while((n)>1):
      lii=[]
      for j in range(1,n+1):
        if(j%2==0):
            lii.append(l[j-1])
      n=len(lii)
      l=[]
      l=lii.copy()
    print(*lii)

        
        
    
