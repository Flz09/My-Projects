array=[1,2,3,4,5,6,7,8]
arraylength=len(array)
#to delete more change the range.
for i in range(3):
  del[array[(arraylength-i)-1]]
print(array)

#this is adding 2.2 to the first 3 index's.
for i in range(3):
  array[i] = array[i] + 2.2
print(array)