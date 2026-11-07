# utopian tree program (problem based on the two different seasons in like spring and summer season .

spring season = height * 2 
summer season = height + 1 

n = int(input("Enter number of cycels: "))

height = 1      

for i in range(n):
  if i % 2 == 0:
    height = height * 2 
  else:
    height = height + 1 
    
print("Tree height :", height)
