import time
import matplotlib.pyplot as plt


def show(immeubles,skyline):
    # Une fonction permettant d'afficher les immeubles en bleu et une
    # skyline en rouge par dessus.
    for (x0,H,x1) in immeubles:
        X = [x0,x0,x1,x1]
        Y = [0,H,H,0]
        plt.fill(X,Y,color='c',edgecolor="b")
    X = []
    Y = [0]
    lastx = 0
    for (x,h) in skyline :
        X.append(x)
        X.append(x)
        Y.append(h)
        Y.append(h)
        lastx = x
    X.append(lastx)
    plt.plot(X,Y,color='r',linestyle="--")
    
    plt.show()





# QUESTION 1
def cherche_etoile(a):
    if not "*" in a:
        return False
    return cherche_etoile_rec(a, 0, len(a)-1)

def cherche_etoile_rec(a, i, j):
    # cas de base
    if i == j:
        if a[i] == "*":
            return i
        else:
            return -1
    # cas récursif
    else:
        m = (i+j)//2
        if a[m] == "*":
            return cherche_etoile_rec(a, i, m)
        else:
            return cherche_etoile_rec(a, m+1, j)
        

# QUESTION 2
def exp(x, n):
    count = 1
    for i in range(n):
        count *= x
    return count

# QUESTION 3
def speedexp(x, n):
    # recursive way to calculate x^n
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n%2 == 0:
        return speedexp(x*x, n//2)
    else:
        return x * speedexp(x*x, (n-1)//2)
    
    


# QUESTION 5
def skyline_naif(immeubles):
    skyline = []
    # get the min and max x
    minx = immeubles[0][0]
    maxx = immeubles[0][2]
    for (x0, _, x1) in immeubles:
        if x0 < minx:
            minx = x0
        if x1 > maxx:
            maxx = x1
    # for each x, find the max height
    for x in range(minx, maxx+1):
        maxh = 0
        for (x0, h, x1) in immeubles:
            if x0 <= x and x < x1 and h > maxh:
                maxh = h
        if len(skyline) == 0 or maxh != skyline[-1][1]:
            skyline.append((x, maxh))
    return skyline


# QUESTION 6
def fusion_skylines(skyline1, skyline2):
    skyline = []
    i = 0
    j = 0
    while i < len(skyline1) and j < len(skyline2):
        if skyline1[i][0] < skyline2[j][0]:
            skyline.append(skyline1[i])
            i += 1
        elif skyline1[i][0] > skyline2[j][0]:
            skyline.append(skyline2[j])
            j += 1
        else:
            if skyline1[i][1] > skyline2[j][1]:
                skyline.append(skyline1[i])
            else:
                skyline.append(skyline2[j])
            i += 1
            j += 1
    if i < len(skyline1):
        skyline += skyline1[i:]
    if j < len(skyline2):
        skyline += skyline2[j:]
    return skyline



# QUESTION 7
def skyline_dpr(immeubles):
    skyline = []
    if len(immeubles) == 1:
        (x0, h, x1) = immeubles[0]
        skyline.append((x0, h))
        skyline.append((x1, 0))
        return skyline
    else:
        skyline1 = skyline_dpr(immeubles[:len(immeubles)//2])
        skyline2 = skyline_dpr(immeubles[len(immeubles)//2:])
        return fusion_skylines(skyline1, skyline2)
    


if __name__ == "__main__":
    a = "###############*"
    print(cherche_etoile(a))
    print(exp(2, 3))


    # QUESTION 4
    now = time.time()
    speedexp(13, 50000)
    print("SpeedExp :" + str(time.time() - now))
    now = time.time()
    exp(13, 50000)
    print("Exp :" + str(time.time() - now))


    immeubles= [(3,13,5),(1,11,5),(12,7,16),(14,3,25),(19,18,22),(2,6,7),(23,13,29),(23,4,28)]
    skyline =  [(1,11),(3,13),(9,0),(12,7),(16,3),(19,18),(22,3),(23,13),(29,0)]

    show(immeubles,skyline_naif(immeubles))
    show(immeubles,fusion_skylines(skyline_naif(immeubles), skyline_naif(immeubles)))
    # show(immeubles,skyline_dpr(immeubles))