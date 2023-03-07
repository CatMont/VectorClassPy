import array


class Vector:
    def __init__(self): #initialize array
        self.arrays = array.array('i', [0, 0])
    def printArray(self):
        print(self.arrays)

    def length(self): #return length of array
        x = len(self.arrays)
        return x

    def contains(self, item): #iterate through every i item in array, if i = item return True
        for i in self.arrays:
            if i == item:
                return True
                break;
        else:
            return False

    def getitem(self, ndx):#retrieve item at index ndx if ndx is within index of array
        if ndx < len(self.arrays):
            return self.arrays[ndx]
        else:
            return "Index out of range"

    def setitem(self, ndx, item): #set item in array at ndx to value item
        if ndx < len(self.arrays):
            self.arrays[ndx] = item
            return self.arrays
        elif ndx == (len(self.arrays)):
            self.arrays.append(item)
            return self.arrays
        else:
            return "Index out of range"

    def append(self, item): #add element to the end of array
        self.arrays.append(item)
        return self.arrays

    def insert(self, ndx, item):  #insert item at index within range of length +1
        if ndx < len(self.arrays):
            self.arrays.insert(ndx, item)
            return self.arrays
        else:
            return "Index out of range"
    def remove(self, ndx): #remove item  index ndx
        if ndx < len(self.arrays):
            self.arrays.remove(ndx)
            return self.arrays
        else:
            return "Index out of range"

    def indexOf(self, item): #return index of item if item is in array
        for i in range(len(self.arrays)):
            if self.arrays[i] == item:
                return i
        else:
            return "item not in list"
    def extend(self, otherVector): #extend array with list input
        self.arrays.extend(otherVector)
        return self.arrays
    def subVector(self, frm, to): #create a subvector using the elements in array from the first number given to the function to the second number + 1
        subVec = Vector()
        subVec.arrays = self.arrays[frm : (to + 1)]
        return subVec.arrays

V = Vector()
V.printArray()
print("Test Length")
print(V.length())
print("\n Test Contains")
print(V.contains(0))
print("\n Test Get Item")
print(V.getitem(1))
print("\n Test Set Item")
print(V.setitem(2,1))
print("\n Test Append")
print(V.append(4))
print("\n Test remove")
print(V.remove(1))
print("\n Indexof")
print(V.indexOf(4))
print("\n Extend")
print(V.extend([1, 2, 3]))
V.printArray()
print("\n subVector")
print(V.subVector(1, 3))
