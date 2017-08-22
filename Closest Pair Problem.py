def calcdistance(A,B):
    x1,y1 = A
    x2,y2 = B
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def savepoints(x,y):
    global xlist, ylist
    xlist.append(x)
    ylist.append(y)
    
def getpoints(n):
    global xlist, ylist
    xlist = [] 
    ylist = [] 
    
    for counter in range(n):
        print("Point #" + str(counter+1))
        while True:
            try:
                x = float(input("What's the X value?"))
            except: 
                print ("Looks like you did not enter float number!")
                continue
            else:
                break
        while True:
            try:
                y = float(input("What's the Y value?"))
            except: 
                print ("Looks like you did not enter float number!")
                continue
            else:
                break
        
        savepoints(x,y)
        points = [xlist,ylist]
    return points

def findclosest():
    global xlist,ylist, valueslist,a_list,b_list,points
    
    valueslist= []
    a_list = []
    b_list = []
    for i in range(len(xlist)):
    
        x1point = int(points[0][i])
        y1point = int(points[1][i])
    
        A = (x1point,y1point)
    
        for i1 in range(len(xlist)):
        
            if i ==i1:
                break
        
            x2point = int(points[0][i1])
            y2point = int(points[1][i1])
        
            B = (x2point,y2point)
        
            value = calcdistance(A,B)
            #print("value for i,i1 = " + str(i) + "," + str(i1) + " is " + str(value))
        
            valueslist.append(float(value)) 
            a_list.append(i)
            b_list.append(i1)
    minindex = valueslist.index(min(valueslist))
    #return min(valueslist)
    return ('The closest points are #' +  str(a_list[minindex]+1) + ' and #' + str(b_list[minindex]+1) + ": distance is " + str(min(valueslist)))

def run():
    global points
    
    while True:
            try:
                num = int(input("How many points to check?"))
            except: 
                print ("Only integers please!")
                continue
            else:
                break
    points = getpoints(num)
    result = findclosest()
    return result

#Test
run()