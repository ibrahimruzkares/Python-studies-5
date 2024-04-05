numbers = [1, 2, 3, 4, 5, 6, 7]

powers_of_two = [number ** number for number in numbers]
print(powers_of_two)


powers_of_two2 = [number ** number for number in range(1,7)]
print(powers_of_two2)


powers_of_two2 = [number ** number for number in range(1,7) if number % 2 == 0]
print(powers_of_two2)