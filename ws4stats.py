import sys

# open file provided in argument to read
try:
	f = open(sys.argv[1], 'r')
except IOError as err:
	print(std(err))
	exit()
except IndexError as err:
	print(std(err))
	exit()

fp = f.readlines()
flen = len(fp) # cache length so we don't have to calculate it every time

total = 0

# get mean first
for line in fp:
	total = total + int(line)

mean = total / float(flen)

total = 0
for line in fp:
	total = total + ((int(line) - mean) ** 2)

variance = total / float(flen - 1)

print("Mean:	" + str(mean) + "\n")
print("Variance:	" + str(variance) + "\n")
	


