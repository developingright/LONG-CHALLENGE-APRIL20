for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    point = []
    for i in range(len(a)):
        if a[i]%4==0:
            point.append(i)
            point.append(i)
        elif a[i]%2==0:
            point.append(i)
    r =0
    count=0
    for i in range(len(a)):
##        print("i->",i)
        if a[i]%2==0 and a[i]%4!=0:
            if r+1<len(point) :
                count+= (n-point[r+1])
                #print("this",count)
            r+=1
##            print(count,"r is ",r)
        elif a[i]%2==0 and a[i]%4==0:
            if r+1<len(point) :
                count+= (n-point[r+1])
                #print("this",count)
            r+=2
##            print(count,"r is ",r)
            
        else:
            if r<len(point):
                if r+1<len(point) and i<point[r]:
                    count+= 1*(point[r]-i)+1*(n-point[r+1])
                else:
                    count+=1*(point[r]-i)
            else:
                count+=1*(n-i)
    print(count)
