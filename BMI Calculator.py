# bmi calculator
weight = input('what is your weight (kgs)?')
height = input('What is your height (m)? ')
square_of_the_height = float(height) * float(height)
bmi = int(weight) / int(square_of_the_height)
print(bmi)
