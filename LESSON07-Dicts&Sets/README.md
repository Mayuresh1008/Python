# Python Dictionaries and Sets

## Dictionaries
A **dictionary** in Python is an unordered collection of items, stored as key-value pairs. It allows fast lookups, modifications, and deletions.

### Creating a Dictionary
Dictionaries can be created in multiple ways:
```python
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")
```

### Accessing Dictionary Items
You can access values using keys:
```python
print(band["vocals"])  # Output: Plant
print(band.get("guitar"))  # Output: Page
```

### Dictionary Properties
- Keys must be unique.
- Values can be of any data type.
- Dictionaries are **mutable** (can be changed after creation).
- Order is maintained in Python 3.7+.

### Listing Keys, Values, and Items
```python
print(band.keys())  # Lists all keys
print(band.values())  # Lists all values
print(band.items())  # Lists key-value pairs as tuples
```

### Checking Key Existence
```python
print("guitar" in band)  # True
print("Triangle" in band)  # False
```

### Modifying a Dictionary
```python
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}
```

### Removing Items
```python
print(band.pop("bass"))  # Removes key "bass"
print(band.popitem())  # Removes the last inserted item

del band["drums"]  # Deletes a specific key
band.clear()  # Clears the dictionary
```

### Copying a Dictionary
Shallow Copy:
```python
band2 = band.copy()
```
Using `dict()`:
```python
band3 = dict(band)
```

### Nested Dictionaries
Dictionaries can contain other dictionaries:
```python
member1 = {"name": "Plant", "instrument": "vocals"}
member2 = {"name": "Page", "instrument": "guitar"}

band = {"member1": member1, "member2": member2}
print(band["member1"]["name"])  # Output: Plant
```

---

## Sets
A **set** is an unordered collection of unique elements. It does not allow duplicate values.

### Creating a Set
```python
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
```

### Set Properties
- **Unordered**: No guarantee of element order.
- **No Duplicates**: Duplicate values are automatically removed.

### Adding Elements
```python
nums.add(9)
print(nums)  # Adds 9 to the set
```

### Updating a Set
```python
morenums = {5, 6, 7}
nums.update(morenums)  # Adds multiple elements from another set
```

### Set Operations
#### Merging Sets (Union)
```python
one = {1, 2, 3}
two = {5, 6, 7}
mynewset = one.union(two)
print(mynewset)  # {1, 2, 3, 5, 6, 7}
```

#### Finding Common Elements (Intersection)
```python
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)  # {2, 3}
```

#### Keeping Only Unique Elements (Symmetric Difference)
```python
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)  # {1, 4}
```

---

## Learnings from the Code
- How to create and manipulate dictionaries and sets.
- Different ways to access and modify dictionary items.
- How to remove elements from dictionaries and sets.
- Copying dictionaries correctly to avoid unintended modifications.
- Nested dictionaries and their access methods.
- Set properties and their unique nature.
- How to perform set operations like union, intersection, and symmetric difference.

This knowledge provides a strong foundation for working with **key-value data** and **unique element collections** in Python!

