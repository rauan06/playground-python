a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
 
# Keys in common: A ∩ B
print(a.keys() & b.keys())

# All keys: A ∪ B
print(a.keys() | b.keys())

# Keys not in b: A ∪ B!
print(a.keys() - b.keys())

# Keys not in a: A! ∪ B
print(b.keys() - a.keys())

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)