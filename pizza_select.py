import random 

def findteams(pizavl,p2,p3,p4):
    if pizavl>p2:
        pizavl-=p2
    else:
        return [pizavl,0,0]

    if pizavl>p3:
        pizavl-=p3
    else:
        return [p2,pizavl,0]

    if pizavl>p4:
        pizavl-=p4
    else:
        return [p2,p3,pizavl]

    return [p2,p3,p4]

if __name__ == "__main__":
    (pizavl,t2,t3,t4)=tuple(map(int,input().split()))
    i=0
    tp={}
    filpiz = findteams(pizavl,t2*2,t3*3,t4*4)
    
    while(i<pizavl):
        temppiz = input().split()
        #indg_no = int(temppiz[0])
        indg_tp = temppiz[1:]
        indg_tp.sort()
        tp[i]=indg_tp
        i+=1
    #print(tp)
    #print(filpiz)

    pizchoi = list(tp.keys())
    result={2:[],3:[],4:[]}
    print(int(filpiz[0]/2+filpiz[1]/3+filpiz[2]/4))
    z=0
    while(z<filpiz[0]):
        xrand = random.choice(pizchoi)
        result[2].append(xrand)
        pizchoi.remove(xrand)
        z+=1
    z=0
    while(z<filpiz[1]):
        xrand=random.choice(pizchoi)
        result[3].append(xrand)
        pizchoi.remove(xrand)
        z+=1
    z=0
    while(z<filpiz[2]):
        xrand=random.choice(pizchoi)
        result[4].append(xrand)
        pizchoi.remove(xrand)
        z+=1

    for i,j in result.items():
        if(j==[]): continue
        print(str(i),' '.join(map(str,j)))
