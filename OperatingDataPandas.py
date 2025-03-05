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