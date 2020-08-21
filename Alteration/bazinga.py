import numpy as np


#this is for key
def kbazingaAlgo(b=""):
    lstoutbin=(list(b))

    for i in range(0,len(lstoutbin)//2):
        if lstoutbin[i]=="1":
            lstoutbin[i]="0"
        else:
            lstoutbin[i] = "1"
    for i in range(len(lstoutbin)//2,len(lstoutbin),2):
        if lstoutbin[i]=="1":
            lstoutbin[i]="0"
        else:
            lstoutbin[i]="1"

    return "".join(lstoutbin)


def bazingaAlgo(b,k):
    lstoutbin=(list(b))

    val = int(np.sum(k) ^ len(b))
    val = val % 10

    #selecting bit manupulation method
    if val in [0, 4,7]:
        check = 1
    elif val in [8,5]:
        check = 2
    elif val in [6,1,9]:
        check = 3
    else:
        check = 4

    #bazinga
    if check == 1:
        #toggle
        for i in range(0,len(lstoutbin)//2):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i] = "1"
        #spiral
        for i in range(len(lstoutbin)//2,len(lstoutbin),2):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"

    elif check == 2:
        #spiral
        for i in range(0,len(lstoutbin)//3,2):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"
        #toggle
        for i in range(len(lstoutbin)//3,(len(lstoutbin)//3)+(len(lstoutbin)//3)):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"
        #spiral
        for i in range((len(lstoutbin)//3)+(len(lstoutbin)//3),len(lstoutbin),2):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"

    elif check == 3:
        #toggle
        for i in range(0,len(lstoutbin)//3):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"
        #spiral
        for i in range(len(lstoutbin)//3,(len(lstoutbin)//3)+(len(lstoutbin)//3),2):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"
        #toggle
        for i in range((len(lstoutbin)//3)+(len(lstoutbin)//3),len(lstoutbin)):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"

    elif check == 4:
        #spiral
        for i in range(0,len(lstoutbin)//2,2):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"
        #toggle
        for i in range(len(lstoutbin)//2,len(lstoutbin)):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"

    return "".join(lstoutbin)

def bazingaAlgoPRO(b,k):
    lstoutbin=(list(b))

    val = int(np.sum(k)) 
    val = val % 10

    #selecting bit manupulation method
    if val in [0, 4,7]:
        check = 1
    elif val in [8,5]:
        check = 2
    elif val in [6,1,9]:
        check = 3
    else:
        check = 4

    #bazinga
    if check == 1:
        #toggle
        for i in range(0,len(lstoutbin)//2):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i] = "1"
        #spiral
        for i in range(len(lstoutbin)//2,len(lstoutbin),2):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"

    elif check == 2:
        #spiral
        for i in range(0,len(lstoutbin)//3,2):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"
        #toggle
        for i in range(len(lstoutbin)//3,(len(lstoutbin)//3)+(len(lstoutbin)//3)):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"
        #spiral
        for i in range((len(lstoutbin)//3)+(len(lstoutbin)//3),len(lstoutbin),2):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"

    elif check == 3:
        #toggle
        for i in range(0,len(lstoutbin)//3):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"
        #spiral
        for i in range(len(lstoutbin)//3,(len(lstoutbin)//3)+(len(lstoutbin)//3),2):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"
        #toggle
        for i in range((len(lstoutbin)//3)+(len(lstoutbin)//3),len(lstoutbin)):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"

    elif check == 4:
        #spiral
        for i in range(0,len(lstoutbin)//2,2):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"
        #toggle
        for i in range(len(lstoutbin)//2,len(lstoutbin)):
            if lstoutbin[i]=="1":
                lstoutbin[i]="0"
            else:
                lstoutbin[i]="1"

    return "".join(lstoutbin)
