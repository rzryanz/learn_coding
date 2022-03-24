import random

for i in range(10):

    # random float: 0.0 <= number < 1.0
    a = random.random()
    print(a)

for i in range(10):

    # random float: 10 <= number < 20
    b = random.uniform(10, 20)
    print(b)

for i in range(10):

    # random integer: 100 <= number <= 1000
    c = random.randint(100, 1000)
    print(c)

for i in range(10):

    # random integer: even numbers in 100 <= number < 1000
    d = random.randrange(100, 1000, 2)
    print(d)

t = [1, 2, 3]
print(random.choice(t))
