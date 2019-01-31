from hashlib import sha256
import json
from functools import reduce

Data1 = ['1','2','3','4']
Data2 = ['This is a string']
Data3 = ['Room 12']
Data4 = ["Name:Justice", "Course:Computer Science", "Country:China"]
Data5 = ['Python',35,'Java',32,'Php',36]
Data6 = [114]



def DataHash(data):
    dataPrep = str(json.dumps(data))
    hdata = (sha256(dataPrep.encode())).hexdigest()
    return hdata
    #print ("The Hashed Data is:", hdata)


#DataChain = Data1+Data2+Data3+Data4+Data5+Data6
Data1.append(Data2)
Data1.append(Data3)
Data1.append(Data4)
Data1.append(Data5)
Data1.append(Data6)
# Confirmation.
#   Data 1 is now by DataChain. 
print('')
print(Data1)
HashDataChain = DataHash(Data1)
print("The HashDatachain is:", HashDataChain)



#DataHash(Data6)

Data1 = ['1','2','3','4']

# Ground Zero.
Data1.append(Data2)
print("Data 1 and 2 merged is", Data1)
print("The hash of Data 1 and 2 is: ", DataHash(Data1))
print('')
Data3.append(Data4)
print("Data 3 and 4 merged is", Data3)
print("The hash of Data 3 and 4 is: ", DataHash(Data3))
print('')
Data5.append(Data6)
print("Data 5 and 6 merged is", Data5)
print("The hash of Data 5 and 6 is: ", DataHash(Data5))
print('')

# Ground 1
Data1.append(Data3)
print("This Data now contains Data 1,2 and 3", Data1)
print("The hash is: ", DataHash(Data1))
print('')


# Ground 2 - This is the root of the Merkle Tree.
print('')
Data1.append(Data5)
print("This Data now contains Data 1, 2, 3, 4 and 5", Data1)
print("The Root Hash is: ", DataHash(Data1))




#   Just playing with some data begins. Don't mind me. #
myList = [1,2,3,4]
ans = list(map(lambda x: x-5, myList))

#print("The ans is: ", ans)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
#print(final_list) 

COUNTERS = [1, 2, 3, 4]

m = lambda x,y: x*x*x+y
#print(m(2,1))

def add(x): 
    #print("Inside add method")
    return x+10

result = list(map(add, COUNTERS))

#print("The result of various additions is:", result)

li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
#print (sum) 

#   Play time over. #

