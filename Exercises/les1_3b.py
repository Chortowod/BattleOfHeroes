from random import randint
import names

# 1. Create a list of randomly generated numbers between 1 and 100.
rndlist = []
n = 0
while n < 20:
    rndlist.append(randint(1, 100))
    n+=1

# 2. Based on the first list, generate a second that has the word “High” or “Low”
#  depending on whether the corresponding number in the first list 
# is greater than or less than 50.
highlist = []
for value in rndlist:
    if value == 50:
        highlist.append("Equal")
        continue
    if value > 50:
        highlist.append("High")
    else: 
        highlist.append("Low")

print(rndlist)
print(highlist)

# 3. Generate a list of 100 names.
namelist = []
while n < 100:
    namelist.append(names.get_first_name())
    n+=1

# 4. Generate two new lists.
namelistwith = []
namelistwithout = []

# 5. One with the names where the first character begins with a letter between “a” and “m” 
# with the other lists containing the other names.
for value in namelist:
    if ord(value[0]) > 64 and ord(value[0]) < 78:
        namelistwith.append(value)
    else:
        namelistwithout.append(value)

print(namelistwith, namelistwithout)
