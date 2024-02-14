import string
from typing import List, TypeVar
from os import name, system


def hFunc(key: TypeVar, i: int):
    return (int(key)%4 +3) + i

def HashInsertwFunction(Table: List, key: TypeVar):
    i = 0
    while i != len(Table):
        q= hFunc(key, i)
        if (Table[q] == None or Table[q] == "DELETED"):
            Table[q] = key
            return q
        else: i = i + 1
    raise TypeError("Hash Table Overflow")

def HashSearchwFunction(Table: List, key: TypeVar):
    i = 0
    while i != len(Table) or Table[q] == None or Table[q] == "DELETED":
        q = hFunc(key, i)
        if Table[q] == key:
            return q
        i = i+1
    return "NIL"

def HashInsert(Table: List, key: TypeVar):
    i = 0
    while i != len(Table):
        q= key
        if (Table[q] == None or Table[q] == "DELETED"):
            Table[q] = key
            return q
        else: i = i + 1
    raise TypeError("Hash Table Overflow")

def HashSearch(Table: List, key: TypeVar):
    i = 0
    while i != len(Table) or Table[q] == None or Table[q] == "DELETED":
        q = key
        if Table[q] == key:
            return q
        i = i+1
    return "NIL"

def HashDelete(Table: List, q: int):
    Table[q] = "DELETED"
    
def test1():
    tobeHashed : List[TypeVar] = [4, 16, 2, 9, 5, 3, 10]

    isHashed : List[TypeVar] = 16*[None]
    
    for ele in tobeHashed:
        HashInsertwFunction(isHashed, ele)
        
    for index in range(len(isHashed)):
        print(f"{index} : {isHashed[index]}")
        
    print(f"\nThe index that the element 9 is at is: {HashSearchwFunction(isHashed, 9)} \n")
    
    HashDelete(isHashed, 7)
    print("Deleted the index 7 from the Table. Here is the new table. \n")
    
    for index in range(len(isHashed)):
        print(f"{index} : {isHashed[index]}")
    

def test2():
    tobeHashed : List[TypeVar] = [3, 2, 6, 4, 3, 7, 0]
    isHashed : List[TypeVar] = 16*[None]
    
    for ele in tobeHashed:
        HashInsertwFunction(isHashed, ele)
        
    for index in range(len(isHashed)):
        print(f"{index} : {isHashed[index]}")
        
    print(f"\nThe index that the element 0 is at is: {HashSearchwFunction(isHashed, 0)} \n")
    
    HashDelete(isHashed, 4)
    print("Deleted the index 4 from the Table. Here is the new table. \n")
    
    for index in range(len(isHashed)):
        print(f"{index} : {isHashed[index]}")

test1()

input("Press the <ENTER> key to continue...")
if name == "nt":
    system("cls")
else:
    system("clear")
    
test2()

input("Press the <ENTER> key to continue...")
if name == "nt":
    system("cls")
else:
    system("clear")
    
app : List = 3 * [None]
app[0] = "\tOne application of hashing is when storing prescriptions at a pharmacy. There's a certain amount of boxes for each first letter of a last name. When the prescription is stored, it is stored by its owner's last name. If there is a more common usage of a certain letter that begins a last name, more boxes are added for that case."
app[1] = "\tUser IDs for a company might be stored within a hashtable to easily search for an ID and its accompanying information."
app[2] = "\tGrocery stores sort their products by type and branding. Each isle has a type of product it houses, and within them, there are brands."

for index in range(3):
    print(app[index])
    
print("Using appplication 2, here is an example.")

userIDS_Unsorted : List[int] = [3, 7, 1, 2, 5, 8]
userIDS_Sorted : List[TypeVar] = 10 * [None]

for ele in userIDS_Unsorted:
        HashInsertwFunction(userIDS_Sorted, ele)

for index in range(len(userIDS_Unsorted)):
    print(f"{index} : {userIDS_Unsorted[index]}")
        
for index in range(len(userIDS_Sorted)):
    print(f"{index} : {userIDS_Sorted[index]}")