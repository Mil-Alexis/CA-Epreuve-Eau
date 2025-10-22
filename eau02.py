def twoNumbersCombination():
	combinations = []
	for firstNumber in range(0, 100):
		for secondNumber in range(0, 100):
			combinations.append(f"{firstNumber:02} {secondNumber:02}")
	return combinations

print(twoNumbersCombination())