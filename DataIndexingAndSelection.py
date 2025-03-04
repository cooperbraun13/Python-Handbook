""" 
Data Selection in Series
"""
# SERIES AS DICTIONARY
# Like a dictionary, the Series object provides a mapping from a collection of keys to a collection of values
import pandas as pd
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=["a", "b", "c", "d"])
print(data)
print(data["b"])

# Can also use dictionary-like Python expressions and methods to examine the key/indices and values
print("b" in data)
print(data.keys())
print(list(data.items()))

# Series objects can be modified with a dictionary-like syntax
# You can extend a Series by assigning to a new index value
data["e"] = 1.25
print(data)

print("---------------------------------")
# SERIES AS ONE-DIMENSIONAL ARRAY
# A Series builds on this dictionary-like interface and provides array-style item selection via slices, masking, and fancy indexing
# Slicing by explicit index
print(data["a":"c"])

# Slicing by implicit integer index
print(data[0:2])

# Masking
print(data[(data > 0.3) & (data < 0.8)])

# Fancy indexing
print(data[["a", "e"]])

# When slicing with an explicit index (data["a":"c"]), the final index is included 
# When slicing with an implicit index (data[0:2]), the final index is excluded

print("---------------------------------")
# INDEXERS: LOC and ILOC
# If your Series has an explicit integer index, and indexing operation such as data[1] will use the explicit indices,
# while a slicing operation like data[1:3] will use the implicit Python-style index
data = pd.Series(["a", "b", "c"], index=[1, 3, 5])
print(data)

# Explicit index when indexing
print(data[1])

# Implicit index when slicing
print(data[1:3])

# Because this is confusing, Pandas provides some special indexer attributes that explicitly expose certain indexing schemes.
# The loc attribute allows indexing and slicing that always references the explicit index
# Label based indexing, inclusive slicing
print(data.loc[1])

print(data.loc[1:3])

# The iloc attribute allows indexing and slicing that always references the implicit Python-style index
# Integer position-based indexing, exclusive slicing
print(data.iloc[1])

print(data.iloc[1:3])

# Explicit is better than implicit!

print("*********************************")

"""
Data Selection in DataFrame 
"""
# DATAFRAME AS A DICTIONARY
area = pd.Series({"California": 423967, "Texas": 695662,
                  "New York": 141297, "Florida": 170312,
                  "Illinois": 149995})
pop = pd.Series({"California": 38332521, "Texas": 26448193,
                 "New York": 19651127, "Florida": 19552860,
                 "Illinois": 12882135})
data = pd.DataFrame({"area": area, "pop": pop})
print(data)

# The individual Series that make up the columns of the DataFrame can be accessed via dictionary-style indexing of the column name
print(data["area"])

# We can also use attribute-style access with column names that are strings
print(data.area)

# This attribute-style column access actually accesses the exact same object as the dictionary-style access
print(data.area is data["area"])

# Dictionary-style syntax can also be used to modify the object
data["density"] = data["pop"] / data["area"]
print(data)

print("---------------------------------")

# DATAFRAME AS TWO-DIMENSIONAL ARRAY
# We can examine the raw underlying data using the values attribute
print(data.values)

# Transpose the full DataFrame to swap rows and columns
print(data.T)

# Passing a single index to an array accesses a row
print(data.values[0])

# Passing a single index to a DataFrame accesses a column
print(data["area"])

# Using the iloc indexer, we can index the underlying array as if it is a simple NumPy array,
# but the DataFrame index and column labels are maintained in the result
print(data.iloc[:3, :2])

# Using the loc indexer can index the underlying data in an array-like style but using
# the explicit index and column names
print(data.loc[:"Illinois", :"pop"])

# In the loc indexer we can combine masking and fancy indexing
print(data.loc[data.density > 100, ["pop", "density"]])

# Any of these indexing conventions may also be used to set or modify values;
# this is done in the standard way from NumPy
data.iloc[0, 2] = 90
print(data)

print("---------------------------------")

# ADDITIONAL INDEXING CONVENTIONS
# Indexing refers to columns, slicing refers to rows
print(data["Florida":"Illinois"])

# Such slices can also refer to rows by number rather than index
print(data[1:3])

# Direct masking operations are also interpreted row-wise rather than column-wise
print(data[data.density > 100])
print(data[data.density < 100])
    