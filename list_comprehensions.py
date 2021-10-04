# Exercise 1 -
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
uppercased_fruits = []
for fruit in fruits:
    uppercased_fruits.append(fruit.upper())
print(uppercased_fruits)

# Exercise 2 -
capitalized_fruits = []
for fruit in fruits:
    capitalized_fruits.append(fruit.capitalize())
print(capitalized_fruits)

# Exercise 3 -
def is_vowel(char):
  if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
    return True
  else:
    return False

def count_vowels(something):
    countvs = []
    letters = list(something)
    for letter in letters:
        if is_vowel(letter):
            countvs.append(letter)
    return len(countvs)

fruits_with_more_than_two_vowels = []
for fruit in fruits:
    if count_vowels(fruit) > 2:
        fruits_with_more_than_two_vowels.append(fruit)
print(fruits_with_more_than_two_vowels)

# Exercise 4 -
fruits_with_only_two_vowels = []
for fruit in fruits:
    if count_vowels(fruit) == 2:
        fruits_with_only_two_vowels.append(fruit)
print(fruits_with_only_two_vowels)

# Exercise 5 -
more_than_five = []
for fruit in fruits:
    if len(fruit) > 5:
        more_than_five.append(fruit)
print(more_than_five)

# Exercise 6 -
exactly_five = []
for fruit in fruits:
    if len(fruit) == 5:
        exactly_five.append(fruit)
print(exactly_five)

# Exercise 7 -
less_than_five = []
for fruit in fruits:
    if len(fruit) < 5:
        less_than_five.append(fruit)
        print(len(fruit))
print(less_than_five)

# Exercise 8 -
count_char = [len(fruit) for fruit in fruits]
print(count_char)

# Exercise 9 - 
def contains_a(fruit):
    return len([letter for letter in fruit if letter == 'a']) > 0
fruits_with_letter_a = [fruit for fruit in fruits if contains_a(fruit)]
print(fruits_with_letter_a)

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Exercise 10 - 
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

 # Exercise 11 - 
odd_numbers = []
for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)
print(odd_numbers)

# Exercise 12 - 
positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)
print(positive_numbers)

# Exercise 13 - 
negative_numbers = []
for number in numbers:
    if number < 0:
        negative_numbers.append(number)
print(negative_numbers)

# Exercise 14 -
two_or_more_numerals = [number for number in numbers if len(str(abs(number))) >= 2]
print(two_or_more_numerals)

# Exercise 15 - 
numbers_squared = [number**2 for number in numbers]
print(numbers_squared)

# Exercise 16 - 
odd_negative_numbers = [number for number in numbers if (number % 2 != 0) and (number <0)]
print(odd_negative_numbers)

# Exercise 17 - 
numbers_plus_5 = [number + 5 for number in numbers]
print(numbers_plus_5)
















