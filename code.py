# goals of the project
# read the CSV file
# skip invalid rows
# count valid vs invalid
# compute min / max / average
# not crash

f = open("data.csv")

valid = 0
invalid = 0
total =0
min = 100
max = -100

next(f)
# read the file
for line in f:
    try:
        int(line)
        # print(line) #prints the valid rows which are numbers
        total+=int(line)
        valid+=1 #keeps the count of valid rows
        if int(line)<min:
            min = int(line)
        if int(line)>max:
            max = int(line)
    except ValueError:
        invalid+=1
        pass

print(valid ,"are valid values")
print(invalid, "are invalid values")
if (valid!=0):
    print("Average is " ,total/valid)
print("Maximum value is ", max)
print("Minimum value is ", min)

    