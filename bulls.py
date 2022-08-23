import random

def digits(num):
	return [int(i) for i in str(num)]
		
def noDuplicate(num):
	num_dig = digits(num)
	if len(num_dig) == len(set(num_dig)):
		return True
	else:
		return False

def generateNum():
	while True:
		num = random.randint(1000,9999)
		if noDuplicate(num):
			return num

def bullsCows(num,guess):
	bull_cow = [0,0]
	num_dig = digits(num)
	guess_dig = digits(guess)
	
	for i,j in zip(num_dig,guess_dig):
		
		if j in num_dig:
		
			if j == i:
				bull_cow[0] += 1
			
			else:
				bull_cow[1] += 1
				
	return bull_cow
	
	
num = generateNum()
guess = 0000
score = 0
print("ENTER 0000 for the answer")
while guess != num:
	try :
		guess = int(input("Enter your guess: "))
		score += 1
		if not noDuplicate(guess):
			print("Number should not have repeated digits. Try again.")
			continue
		if (guess < 1000 or guess > 9999) and guess != 0000:
			print("Enter 4 digit number only. Try again.")
			continue
		
		bull_cow = bullsCows(num,guess)
		print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")

		if bull_cow[0] == 4:
			print("You guessed right!")
			print(f"It took you {score} tries.")
			break
		elif guess == 0000:
			print(f"You gave up and looked for the Number. Number was {num}")
	except ValueError :
		print("Enter Only Numbers! \n")
