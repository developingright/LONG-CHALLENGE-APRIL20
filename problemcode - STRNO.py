import math
for _ in range(int(input())):
    x,k = map(int,input().split())
    l = []
    i = 1
    flag = True
    while i <= math.sqrt(x): 
          
        if (x % i == 0) : 
              
            if (x / i == i) : 
                l.append(i)
            else :  
                l.append(x//i)
                l.append(i)
        i = i + 1
    l.sort()
    c =0
    for i in range(1,len(l)):
        if x!=1 and x%l[i]==0:
            for j in range(10**6+1):
                if x%l[i]==0:
                        c+=1
                        x=x//l[i]
                        if c==k:
                            flag =False
                            break
                else:
                        break
        if flag==False:
            break
                
    if c == k:
        print(1)
    else:
        print(0)
