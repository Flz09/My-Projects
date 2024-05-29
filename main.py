array=[1,2,3,4,5,6,7,8]
arraylength=len(array)
print('Before:\n',array)
for i in range(arraylength):
  array[i]=array[i]+2
print('After:\n',array)