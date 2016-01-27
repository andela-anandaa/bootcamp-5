def num_to_words(n):
    n = str(n)
    key = 'zero one two three four five six seven eight nine'.split()
    return ' '.join([key[int(i)] for i in n])

# tests
print num_to_words(120)
print num_to_words(253)
