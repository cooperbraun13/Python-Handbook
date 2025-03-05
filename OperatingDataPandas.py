"""
Ufuns: Index Preservation 
"""
import pandas as pd
import numpy as np

rng  = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4))
print(ser)

df = pd.DataFrame(rng.randint(0, 10, (3, 4)),
                  columns=["A", "B", "C", "D"])
print(df)

# If we apply a NumPy ufunc on either of these objects, the result will be another
# Pandas object with the indices preserved
print(np.exp(ser))

# Slightly more complex
print(np.sin(df * np.pi / 4))

"""
Ufuncs: Index Alignment 
"""
# For binary operations on two Series or DataFrame objects, Pandas will align
# indices in the process of performing the operation
# INDEX ALIGNMENT IN SERIES
area = pd.Series({"Alaska": 1723337, "Texas": 695662,
                  "California": 423967}, name="area")
population = pd.Series({"California": 38332521, "Texas":26448193,
                        "New York": 19651127}, name="population")

print(population / area)

# The resulting array contains the union of indices of the two input arrays

print(area.index, population.index)

# Any item for which one or the other does have an entry is marked with NaN,
# or "Not a Number", which is how Pandas marks missing data

A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
print(A + B)

# If using NaN values is not the desired behavior, the fill value can be modified
# using appropriate object methods in place of the operatings

print(A.add(B, fill_value=0))

# INDEX ALIGNMENT IN DATAFRAME
A = pd.DataFrame(rng.randint(0, 20, (2, 2)),
                 columns=list("AB"))
print(A)

B = pd.DataFrame(rng.randint(0, 10, (3, 3)),
                  columns=list("BAC"))
print(B)

print(A + B)

fill = A.stack().mean()
A.add(B, fill_value=fill)

print(A + B)

""" 
Ufuncs: Operations Between DataFrame and Series
"""