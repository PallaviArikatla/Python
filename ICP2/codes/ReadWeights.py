inpList = []
outList = []
numElem = int(input("Enter number of elements:"))
for i in range(numElem):
    tempElem = float(input("enter {} for the input list:". format(i+1)))
    inpList.append(tempElem)
    outList = [i*0.453592 for i in inpList]
    print("input list(lbs): {}\noutput list(kgs): {}".format(inpList,outList))