# goals of the project
# read the CSV file
# skip invalid rows
# count valid vs invalid
# compute min / max / average
# not crash


f = open("data.csv")

valid = 0
invalid = 0
# read the file
for line in f:
    try:
        int(line)
        print(line) #prints the valid rows which are numbers
        valid+=1 #keeps the count of valid rows
    except ValueError:
        invalid+=1
        pass

print(valid ,"are valid values")
print(invalid, "are invalid values")


    