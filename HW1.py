# Q1
def count_vowels(words):
    num = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in words:
        if letter in vowels:
            num += 1
    return num


# Q4
def sum_of_integers(a, b):
    return a + b


if __name__ == '__main__':
    # Q2
    animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
    for animal in animals:
        print(animal.upper())

    # Q3
    for i in range(1, 21):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
