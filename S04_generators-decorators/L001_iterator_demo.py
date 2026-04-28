

class CountTo:
    def __init__(self, max_value):
        self.max = max_value

    def __iter__(self):
        return CountToIterator(self.max)


class CountToIterator:
    def __init__(self, max_value):
        self.max = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration



# EXAMPLE 1: Iterating over a list of foods and skipping duplicates
print ("========================================================== ")
print ("Example 1: ")
print ("========================================================== ")
my_foods = ["apple", "banana", "cherry"]

for food in my_foods:
    for food2 in my_foods:
        if food == food2:
            print(f"Skipping duplicate food: {food}")
            continue
        print(f"Cooking {food} with {food2}")


# EXAMPLE 2: 
print ("========================================================== ")
print ("Example 2: ")
print ("========================================================== ")
counter = CountToIterator(5)

for count in counter:
    for count2 in counter:
        print(f"Count: {count} and {count2}")



# EXAMPLE 3: 
print ("========================================================== ")
print ("Example 3: ")
print ("========================================================== ")
counter = CountToIterator(5)

for count in CountToIterator(5):
    for count2 in CountToIterator(5):
        print(f"Count: {count} and {count2}")



# EXAMPLE 4: 
print ("========================================================== ")
print ("Example 4: ")
print ("========================================================== ")
counter = CountTo(5)

for count in counter:   # for runs the __iter__() method of CountTo, which returns a new CountToIterator    
    for count2 in counter:     # for runs again the __iter__() method of CountTo, which returns a new CountToIterator    
        print(f"Count: {count} and {count2}")
