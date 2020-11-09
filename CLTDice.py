import sys
import random

def roll(n, trials):
	sums = []
	for j in range(trials):
		currSum = 0
		for i in range(n):
			roll = random.randint(1,6)
#			print(roll)
			currSum += roll
		sums.append(currSum)
#		print("End Sample")

	return sums

def histoInfo(list, minValue, maxValue):
	info = []
	for i in range(minValue, maxValue + 1):
		count = 0
		for sum in list:
			if sum == i:
				count += 1
		info.append(count)
	return info

def histoPrinto(list, minValue, maxValue):
	zero = True
	timeSinceZero = 0
	eX = (minValue + maxValue) / 2
	distance = 0
	print("Histogram\n----------------------")
	for i in range(minValue, maxValue + 1):
		if list[i - minValue] != 0 and zero:
			zero = False
			timeSinceZero = 0
			distance = eX - (i - minValue)

		if not zero:
			if i == int(eX):
				print("\u001B[31m",end="")

			print(f"{str(i):>4}" + ":" + "+" * list[i - minValue], end = "")
			print("\u001B[0m")

			if list[i - minValue] == 0:
				timeSinceZero += 1

			if (eX + distance - minValue) < i:
				break


if len(sys.argv) != 3:
	print("CLTDice.py is used with the following command string:\n" + 
		"$ python CLTDice.py (Sample Size) (Number of Trials)\n" + 
		"i.e. $ python CLTDice.py 2 5")

else:
	n = (int)(sys.argv[1])
	t = (int)(sys.argv[2])
	list = roll(n, t)
#	print(list)
	info = histoInfo(list, n, 6 * n)
	histoPrinto(info, n, 6 * n)
