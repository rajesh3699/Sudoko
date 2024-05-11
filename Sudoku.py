import random
valid=[1,2,3,4,5,6,7,8,9]

#Function to find the empty spaces on grid
def emptyLocation(grid1,empty):
    for row in range(9):
        for col in range(9):
            if grid1[row][col]==0:
                empty[0]=row
                empty[1]=col
                return True
    return False
#Function to check if row has the number
def notInRow(grid1,row,num):
    for i in range(9):
        if grid1[row][i]==num:
            return False

    return True

#Function to check if column has number
def notInCol(grid1,col,num):
    for i in range(9):
        if grid1[i][col]==num:
            return False

    return True

#Function to check if box has number
def notInBox(grid1,row,col,num):
    r=row - row%3
    c=col-col%3
    for i in range(3):
        for j in range(3):
            if grid1[i+r][j+c]==num:
                return False
    return True

#Function to check all
def safe(grid1,row,col,num):
    return all([notInBox(grid1,row,col,num),notInRow(grid1,row,num),notInCol(grid1,col,num)])

#Solve the grid
def solver(grid1):
    empty=[0,0]
    if not emptyLocation(grid1,empty):
        return True
    r=empty[0]
    c=empty[1]
    checking=valid[:]
    while len(checking)!=0:
        n=random.choice(checking)
        checking.remove(n)
        if safe(grid1,r,c,n):
            grid1[r][c]=n
            if solver(grid1):
                return True

            grid1[r][c]=0

    return False

#Generate sudoko
def makeSudoko(k):
    grid1=[[0 for i in range(9)]for j in range(9)]
    rr=random.randint(0,8)
    rc=random.randint(0,8)
    rn=random.choice(valid)
    grid1[rr][rc]=rn
    if solver(grid1):
        remove(grid1,k)
        return grid1
    return 0

def remove(grid1,k):
    count=0
    while count<k:
        rr=random.randint(0,8)
        rc=random.randint(0,8)
        if grid1[rr][rc]!=0:
            grid1[rr][rc]=0
            count+=1


def printSudoko(su):
    kj=1
    ki=1
    for i in su:
        for j in i:
            print(j," ",end='')
            if kj%3==0:
                print("  ",end='')
            kj+=1
        print()
        if ki%3==0:
            print()
        ki+=1



numberOfSudoko=int(input("How many sudoko u want"))
sol=[]
for i in range(numberOfSudoko):
    s=makeSudoko(int(input("What difficulty easy=10,medium=20,hard=30,expert=45?")))
    printSudoko(s)
    solver(s)
    sol.append(s)

for i in range(numberOfSudoko):

    choice=input("press enter for solution of sudoku {}".format(i+1))
    printSudoko(sol[i])




