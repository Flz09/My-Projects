array=[1,2,4,5,6,7,8,9]
arraylength=len(array)
arraymax=array[0]

for i in range (arraylength):
  if array[i]>arraymax:
    arraymax = array[i]
print(arraymax)