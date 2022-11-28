# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    #check if line is starting from required string
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    #slice string
    lineRange = line[18+1:]
    lineRange.strip()

    #convert type to float
    numFloat = float(lineRange)

    #update the line count
    count = count + 1
    #Calculate the sum 
    total = numFloat + total

average = total / count
print("Average spam confidence:", float(average))
