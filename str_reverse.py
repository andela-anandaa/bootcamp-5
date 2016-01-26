def reverse(w):
    '''Returns the reverse of a string
    using slicing
    '''
    return w[::-1]

def swap(list_, i, j):
    list_[i], list_[j] = list_[j], list_[i]

def reversex(s):
    new_s = list(s)
    length = len(new_s)
    for i in range(length // 2):
        swap(new_s, i, length - i - 1)

    return "".join(new_s)

# examples
print reversex("andela")
print reverse("hello")
