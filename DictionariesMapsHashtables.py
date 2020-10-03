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

d["four"] = 4

d.keys()
#odict_keys(['one', 'two', 'three', 'four'])



# The defaultdict class is another dictionary sublcass that accepts a callable in its constructor whose return value will be used if a requested key cannot be found
from collections import defaultdict
dd = defaultdict(list)

#accessing a missing key creates it and inititalizes it using the default factory, ie the list
dd["dogs"].append("Rufus")
dd["dogs"].append("Kathrin")
dd["dogs"].append("Mr Sniffles")

dd["dogs"]
['Rufus', 'Kathrin', 'Mr Sniffles']


# collections.ChainMap data structure groups multiple dictionaries into a single mapping. Lookups search the underlying mappings one by one until a key is found.
from collections import ChainMap
dict1 = {"one": 1, "two": 2}
dict2= {"three": 3, "four": 4}
chain = ChainMap(dict1, dict2)

chain
#ChainMap({'one': 1, 'two': two}, {'three': 3, 'four': 4})

#ChainMap searches each collection in the chain
#from the left to right until it finds the key (or fails):
chain["three"]
#3

chain["one"]
#1

chain["missing"]
#Returns an error

