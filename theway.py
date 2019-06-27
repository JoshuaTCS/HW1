
intNum=(input("Input number: "))
numArray=[]
length=len(intNum)
mil=["daan ", "libo ", "milyon ", "bilyon "]
ten=["","labing ","dalawampu ","tatlumpu ","apatnapu ","limampu ","animnapu ","pitumpu ", "walumpu ","siyamnapu "]
one=["", "isa ","dalawa ","tatlo ","apat ","lima ","anim ","pito ","walo ","siyam ", "sampu ","sero "]
for i in range(length):
    numArray.append(int(intNum[i]))

if length==1:
    if intNum==0:
        print(one[numArray[11]])
    else:
        print(one[numArray[0]])
elif length==2:
    if numArray[0]==1 and numArray[1]==0:
        print(ten[0])
    else:
        print(ten[numArray[0]]+one[numArray[1]])
elif length==3:
        print(one[numArray[0]]+mil[0]+ten[numArray[1]]+one[numArray[2]])
elif length==4:
        print(one[numArray[0]]+mil[1]+one[numArray[1]]+ten[numArray[2]]+one[numArray[3]])
elif length==5:
    if numArray[4]==0 and numArray[3]==0 and numArray[2]==0:
        if numArray[0]==1:
            print(one[10] + mil[1])
        else:
            print(one[numArray[0]]+mil[1])
    else:
        print(ten[numArray[0]]+one[numArray[1]]+mil[1]+one[numArray[2]]+mil[0]+ten[numArray[3]]+one[numArray[4]])




       
print(numArray)
