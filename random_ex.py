import random

print(random.randrange(1, 7))
print(random.randrange(1, 7))
print(random.randrange(1, 7))
print(random.randrange(1, 7))

participants = [
    'Vladimir',
    'Oleg',
    'Aleksandr',
    'Vika',
    'Yuliya'
]

print(participants[random.randrange(3)])


print(random.choice(participants))

random.shuffle(participants)
print('Shuffle 1:', participants)
random.shuffle(participants)
print('Shuffle 2:', participants)
random.shuffle(participants)
print('Shuffle 3:', participants)
