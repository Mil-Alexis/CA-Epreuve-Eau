def threeDigitsCombination():
	combinations = []
	for firstDigit in range(0, 10):
		for secondDigit in range(firstDigit + 1, 10):
			for thirdDigit in range(secondDigit + 1, 10):
				 combinations.append(f"{firstDigit}{secondDigit}{thirdDigit}")
	return combinations

print(threeDigitsCombination())