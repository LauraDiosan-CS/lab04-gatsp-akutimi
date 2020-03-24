
from random import uniform,randint,shuffle
from math import sqrt

def generateNewValue(lim1, lim2):
    return randint(lim1, lim2)

def binToInt(x):
    val = 0
    # x.reverse()
    for bit in x:
        val = val * 2 + bit
    return val

def readNet(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(",")
        for j in range(n):
            mat[-1].append(int(elems[j]))
    net["mat"] = mat
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if mat[i][j] >= 1:
                d += 1
            noEdges += mat[i][j]
        degrees.append(d)
    noEdges=noEdges//2
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    f.close()
    return net

def readNetFloat(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(" ")
        for j in range(n):
            mat[-1].append(float(elems[j]))
    net["mat"] = mat
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if mat[i][j] >= 1:
                d += 1
            noEdges += mat[i][j]
        degrees.append(d)
    noEdges=noEdges//2
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    f.close()
    return net



def generateARandomPermutation(n):
    perm = [i for i in range(n)]
    shuffle(perm)
    # pos1 = randint(0, n - 1)
    # pos2 = randint(0, n - 1)
    # perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm


def binaryMaskUniform(dim):
    mask=[]
    for _ in range(dim):
        r=uniform(0,1)
        if r<0.5:
            mask.append(0)
        else:
            mask.append(1)
    return mask

def distantaPuncte(p1,p2):
    return sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

def modifyBerlin():
    f = open("berlin52.txt", "r")
    n = int(f.readline())
    g=open("berlin.txt","w")
    mat=[[0]*n for _ in range(n)]
    listaCoord=[]
    for i in range(n):
        line = f.readline()
        elems = line.split(" ")
        listaCoord.append((float(elems[1]),float(elems[2])))


    for i in range(n):
        for j in range(n):
            if i!=j:
                mat[i][j]=distantaPuncte(listaCoord[i],listaCoord[j])

    g.writelines(str(n) + "\n")
    for el in mat:
        newS = ""
        for nr in el:
            newS += str(nr)
            newS += " "
        newS += "\n"
        g.writelines(newS)
    g.close()
    f.close()



def costDrum(matriceCost,cale):
    #la inceput se va adauga si costul de la mat[cale[-1]][cale[0]]
    n=len(cale)
    cost=0
    for i in range(n): # i incepe de la 0 ca vrem sa adaugam costul [cale[0][cale[n]]
        cost+=matriceCost[cale[i]][cale[i-1]]
    return cost

if __name__=="__main__":
    modifyBerlin()