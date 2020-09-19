#Dictionaries are often called maps/hashmaps/lookup tables/associative arrays
#Dicts allow for the efficient lookup, inerstion and deltion of any object associated with a given key


phonebook = {
  "bob": 7387,
  "alice": 3719,
  "jack": 7052
}

squares = {x: x * x for x in range(6)}

phonebook["alice"]
#3719

squares
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

## Python's dicitonaries are index by keys that can be of any hashable type
## A hashable object has a hash value that doesn't change during it's lifetime

##collections.OrderedDict that remembers the insertion order of keys added to it
import collections
d = collections.OrderedDict(one=1, two=2, three=3)

d
#OrderedDict([('one', 1), ('two', 2), ('three', 3)])