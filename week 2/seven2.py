#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines
#compute the average of those values and produce an output as shown below. 
#Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
cnt = 0
avg = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else:
        pos=line.find(".")
        avg=avg + float(line[pos:pos+6])
        cnt += 1
print("Average spam confidence:",avg/cnt)
