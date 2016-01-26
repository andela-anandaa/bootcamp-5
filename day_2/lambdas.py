# anonymous functions

def f(x):
    return x ** 2

g = lambda x: x ** 2

print g(8)

# return a lambda function

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(10)
g = make_incrementor(12)

print f(20), g(50)

# with list functions
# Do long versions first before use of lambda

foo = [2, 10, 15, 16, 20, 25]


print filter(lambda x: x % 3 == 0, foo)

print map(lambda x: x ** 3, foo)

print reduce(lambda x, y: x + y, foo)

# another example
sentence = 'This is Andela, and it will always be'
words = sentence.split()
lengths = map(lambda word: len(word), words)
print lengths

# Challenge: use reduce to count number of characters in a sentence
