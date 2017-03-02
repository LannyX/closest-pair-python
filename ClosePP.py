from math import sqrt

newP = ()
s = []
number = raw_input("How many points? (please enter 10, 100, 1000):")
if number == "10":
 file = open("10points.txt","r")
elif number == "100":
 file = open("100points.txt","r")
elif number == "1000":
 file = open("1000points.txt","r")

for line in file:
 x = int(line.split(' ')[0])
 y = int(line.split(' ')[1])
 newP = newP + (x,)
 newP = newP + (y,)
 s.append(newP)
 newP = ()

file.close()


def closest_point(s):
    len = s.__len__()
    left = s[0:len/2]
    right = s[len/2:]
    mid = (left[-1][0]+right[0][0])/2.0


    ## left part
    if left.__len__() > 2:
        lmin = closest_point(left)    
    else:
        lmin = left

    ##right part
    if right.__len__() > 2:
        rmin = closest_point(right)   
    else:
        rmin = right

    if lmin.__len__() >1:
        dis_l = distance(lmin)
    else:
        dis_l = float("inf")
    if rmin.__len__() >1:
        dis_2 = distance(rmin)
    else:
        dis_2 = float("inf")

    ##nearest distance  
    d = min(dis_l, dis_2) 

    mid_min=[]
    for i in left:
        if mid-i[0]<=d :   
            for j in right:
                if abs(i[0]-j[0])<=d and abs(i[1]-j[1])<=d:
                    if distance((i,j))<=d:
                        mid_min.append([i,j])   
    if mid_min:
        l=[]
        for i in mid_min:
            l.append({distance(i):i})
        l.sort(key=lambda x: x.keys())
        return (l[0].values())[0]
    elif dis_l>dis_2:
        return rmin
    else:
        return lmin
    

def distance(min):
    return sqrt((min[0][0]-min[1][0])**2 + (min[0][1]-min[1][1])**2)

    
def divide_conquer(s):
    s.sort(cmp = lambda x,y : cmp(x[0], y[0]))
    cpp = closest_point(s)
    print ("The minimum distance is:")
    print distance(cpp)
    print cpp


divide_conquer(s)





