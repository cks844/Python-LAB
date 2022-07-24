tup=(1,2,3,4)
o_tup=()
e_tup=()
for i in range(0,len(tup)):
    if(x[i]%2==0):
        e_tup+=(tup[i],)//To create a tuple with only one item, you have to add a comma after the item,
    else:
         o_tup+=(tup[i],)
print("Original tuple : ",tup)
print("Even tuple : ",e_tup)
print("Odd tuple : ",o_tup)
