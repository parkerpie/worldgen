import random

def nexttran(base):
    ############### FLAG TRANSFORMS ###########################################
    new = 0
    if base == flag1:
        i = random.randint(0,1)
        if i == 1:
            new = base + 10
        else:
            new = base - 1

    elif base == flag2:
        i = random.randint(0,1)
        if i == 1:
            new = base + 10
        else:
            new = base + 1

    elif base == flag3:
        i = random.randint(0,1)
        if i == 1:
            new = base - 10
        else:
            new = base + 1

    elif base == flag4:
        i = random.randint(0,1)
        if i == 1:
            new = base - 10
        else:
            new = base - 1

    return new
    ###########################################################################
    '''elif base > flag2 and base < flag1:
        print "-1, +10, +1"
    elif base % xscale == 0:
        print "+1, +10, -10"
    elif base % xscale == (xscale -1):
        print "-1, +10, -10"
    elif base > flag3 and base > flag4:
        print "-10, -1, +1"

    else:'''

xscale  = 10
yscale  = 10
tilesum = xscale * yscale
mtnfreq = .2

#flag definition
flag1 = (xscale - 1)
flag2 = 0
flag3 = (tilesum - xscale)
flag4 = tilesum

tiles = []

for i in range(tilesum):
    tiles.append("x")


base = False

# MOUNTAIN GEN
for i in range(int(tilesum * mtnfreq)): # for every mountain tile
    if base == False:
        #x_tile = random.randint(0, tilesum)
        x_tile = 0
        tiles[x_tile] = "^"
        base = True

    else:
        nx_tile = nexttran(x_tile)
        x_tile = nx_tile

        print nx_tile
        tiles[nx_tile] = "^"

# PRINT THE TILES

count = 0

for i in range(yscale):
    for i in range(xscale):
        print tiles[count],
        count +=1
    print ""
