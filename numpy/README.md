# NumPy

> Concepts: `Arrays, Indexing, Slicing, NumPy Programming`

**NumPy** is a library for Python that adds support for large multi-dimensional arrays and matrices, along with a vast library of high-level mathematical functions to operate on these arrays. NumPy is used heavily by Python programmers for data analysis, machine learning, and much more. 

The NumPy API is used extensivley in Pandas and most other data science and scientific Python packages. Take time to read over the terminology we'll be using throughout this course.

> `masking` is creating an array of True/False values and using it to only include values of the original array that fufill the conditional requirment.
> `vectorized operations` use built in operators on arrays to run mathematical operations faster with much simpler and easily understandable syntax.
> NaN is used by NumPy as a placeholder for values that are not a number. 

## Installation

Because Anaconda and Miniconda should have automatically installed NumPy, we can write `import numpy as np` to import NumPy into our code. However, if an error occurs, execute `conda install numpy` in the terminal to install the module.

In Java, an *array* is a container object that holds a fixed number of values of a single type. After initalization, its length is fixed. An array can be multidimensional, but must stay homogeneous (one single type). In comparison to a *list*, an array takes up signifigantly less space,are faster when reading or writing, and are used to compute high-level mathematical operations more efficiently than python lists with NumPy.

## Initialization 

NumPy allows many methods to create an array, but we will go over the main ones used throughout this course. The row of an array is the amount of commas that are used for each element. The column of an array is the amount of elements in each row.
> `np.array(object, dtype=None, ndmin=0)`

Where *object* is any array-like sequence (lists, tuples, dictionary), *dtype* is the type of the nested elements of the sequence (bool_, int_ float_, complex_), and *ndmin* specifies the minimum number of dimensions the array has (1D, 2D).
For more information about conceptualizing multi-dimensional arrays, check out this handout [here].

> `np.zeros(shape, dtype=float)`

Where *shape* is the shape of the array (tuple or list), and *dtype* is the data type of the nested elements. This method creates an array object of all zeros, default to the dtype of float64. 

```python
np.zeros((2,5))
array([[0., 0., 0., 0., 0.], [0., 0., 0., 0., 0.]])
```

> `np.ones(shape, dtype=float)`

This method creates an array object of all ones, **defaulting** to the dtype of float64.

```python
np.ones(2, dtype="int32")
array([1, 1])
```

> `np.full(shape, fill_value, dtype=None)`

Where *shape* is the shape of the array, *fill_value* is a scalar you want to fill the array with, and *dtype* is the data type of the nested elements. 

```python 
np.full((2,2), 3)
array([[3, 3], [3, 3]])
```

> `np.arange(start, stop, step, dtype=None)`

Where *start* is the starting number (**inclusive**), *stop* is the ending number (**exlusive**), and *step* is the step. This follows common Python protocol with loops, except with step being able to take non-whole numbers for step size.

```python 
np.arange(3, 12, 2.5)
array([3., 5.5, 8., 10.5])
```

> `np.linspace(start, stop, num=50, endpoint=True, dtype="float64")`

Where *num* is the number of samples to generate, *endpoint* is the boolean value of whether or not *stop* is inclusive. This method creates an array object of a range of evenly-spaced numbers with a total of *num* numbers, including **both** the start and stop, and defaults to float64.

```python 
np.linspace(0, 15, 10, endpoint=False)
array(0., 1.5, 3., 4.5, 6., 7.5, 9., 10.5, 12., 13.5)
```

> `np.random.random((rows, columns))`

Where *rows* is the number of rows and *columns* is the number of columns. This method creates an array of random uniform distribution floats in range [0, 1).

```python 
np.random.random((1,2))
array([[0.42349021, 0.32675097]])
```
## Indexing and Slicing

Indexing for NumPy is the same as with lists with square brackets. 

> 💬 If an array is 1D, singular square brackets with index into the array much like a list. However, if an array is 2D, the order seperates into [rows, columns] when searching the array. 

Slicing through an array like a list, using similar notiation as with indexing. 

```python 
array = np.array([[1, 3, 5], [2, 4, 6], [5, 7, 9]])
print(array[1:, 1:])
array([[4, 6], [7, 9]])
```

## Masking and Vectorized Operations

NumPy allows programmers to use *vectorized operations*, a concise syntax to apply mathematical operations or boolean expressions to an array, which allows for augmentation of any array. 

> 💬 Vectorized operations apply the arithmetic operation to each element in an array. It's applied *elementwise*.

We can use any arithmetic operation on an array using NumPy. Consider the following examples. 

```python 
array = np.array([1, 2, 3])
print(array * 2)
array([2, 4, 6])
```

Pretty cool right! It gets better.

```python 
print(array + array)
array([2, 4, 6])
print(array < 3)
array([True, True, False])
```

> 💬 *Note* NumPy allows for array augmentation, but does **not** change the original array. Instead it returned a new array. This is a common NumPy property that will appear again. 

NumPy also allows for filtering an array to only include a subset of the original. **Masking** uses a boolean expression to create an array of booleans, and any *True* value will be used to index the original array. 

```python 
array = np.linspace(0, 10, 5, dtype="int32")
boolArray = array * 2 == array ** 2
array[boolArray]
array([0, 2])
```

> 💬 Skip the second step and directly insert a boolean expression into an array for shorthand notation.

## Advanced Array Augmentation 

Suppose we want to apply multiple filters to an array, but access to logical operators such as *not*, *and*, or *or* is not available. Let's use the **bitwise operators** ~, |, and & for *not*, *or*, and *and* accordingly instead. 

> 💬 Bitwise operators work only on integers. 

We want to filter an array of integers by two factors. The values 1) must be **less than** 11, and 2) must be odd. We have the following array.

```python 
array = np.arange(1, 14, 3)
print(array)
array([1, 4, 7, 10, 13])
```

First, let's create two boolean arrays representing each value. If both arrays are *True* for some specific value, then we have a match. We'll use our bitwise operators to combine both expressions and then take the sum. 

```python 
np.sum((array % 2 != 0) & (array < 11))
2
```

So there are *two* values that are odd and less than 11. Let's finally filter our original array to accomplish this task.

```python
array[(array % 2 != 0) & (array < 11)]
array([1, 4, 7])
```

Awesome! Finally, let's discuss dealing with missing data.

## NumPy Nan: Dealing with Missing Data

Oftertimes throughout our Python programming career we will encounter missing values when reading data. Rather than using *None* (Python's object None stems from NoneType class), NumPy provides a a floating point constant to represent a missing numeric value. NaN stands for Not a Number, and is **not** the same as *null* or *None*.

We can use the Python keyword *is* to check if two objects are the exact same object. 

```python 
print(5 is int)
False
print(type(5) is int)
True
```

When we inspect NaN, the first fundamental detail to note about np.nan is that np.nan does **not** equal np.nan, but np.nan *is* np.nan.

```python
print(np.nan == np.nan)
False
print(np.nan is np.nan)
True
```

What's the signifigance of this? When using NumPy, we may want to filter out these NaN specific values. Let's try to do this.

```python
array = np.array([1, 3, 5, np.nan, 7, 9, np.nan])
print(array[(array is not np.nan)])
array([ 1., 3., 5., nan, 7., .9, nan])
```

What happened? These *NaN* values did not delete from our array because every value in our array automatically has a dtype of *float64* after conversion. To achieve our desired outcome, 

```python 
print(array[~np.isnan(array)])
array([1., 3., 5., 7., 9.,])
```

> 💬 The np.isnan function is a vectorized function, and therefore can be applied elementwise to filter out our np.nan values.

> ❗ Be aware of a dtype of an array being *object*. Because object is the origin class of all of our other subclasses, this will keep np.nan as equal to itself, returning True rather than False when attempting to filter our np.nan elements using is.

```python 
array = np.array([1, 2, np.nan, 4, np.nan], dtype= object)
print(array[2] is np.nan)
True
```

### Array Attributes and Methods

Array attributes hold information about the array. Below are a few commononly used attributes for arrays.

`.dtype` returns the data type of the elements within an array.
`.ndim` returns the number of dimensions of an array.
`.size` returns the number of elements in an array.
`.shape` returns the shape in the order of an array.

> ❗ Attributes are **not** methods, so no need for () parenthesis at the end. 

`.T` returns the transpose of the original array. Transposing an array / matrix switches each element in our first row into their own column, and every element following the first switches their position according to their placement (row / column).

```python 
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array.T)
array([[1, 4, 7], 
       [2, 5, 8],
       [3, 6, 9]])
````

There are many methods NumPy allows users to implemenet into our programs. Here are a few below.

`.copy()` returns a copy of an array that can be assigned to another variable. 
`.fill(value)` replaces all elements of an array with the specified value but does **not** return it.
`.reshape(rows, columns)` returns an array with the new shape but does not change it. 

Reshape returns an array as seen below.

```python
array = np.array([1, 2, 3, 4, 5, 6])
array.reshape(2, 3)
array([[1, 2, 3], [4, 5, 6]])
```

`.flatten()` returns the array, 'flattened' to condense all elements into a one-dimensional array. Essentially every row is collapsed into one long list.

`.sort()` will sort each element in every row in ascending order.

Use .max, .mean, .min, and .sum to return the data of every elements of an array or a given axis. 

> 💬 Add the axis parameter with a comma, and `axis = num` to specifiy a row.

## NumPy Functions

Although after intializing an array NumPy provides the programmer with many methods to use, there are a few functions NumPy includes that are also important. 

`np.concatenate([array1, array2 ...], axis = None)` joins a sequence of arrays on a given axis. 

```python 
np.concatenate([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], axis = 1)
array[[1, 2, 3, 4], [5, 6, 7, 8]])
np.concatenate([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], axis = 0)
array[[1, 2], [3, 4], [5, 6], [7, 7]])
```

`np.where(condition, arr if true, arr if false)` returns an array in which the elements are replaced or unchanged based on a provided condition.

For instance, `np.where(time <= 60, "State Qualifier", trackTimes)` would switch all values that are 60 or below to the string "State Qualifier".

> 💬 Add another string after "State Qualifier" to provide a new value for any time above 60. 

We can also use NumPy to return an array of values read from a file (typically txt, csv, or tsv) using `loadtxt()`

`np.loadtxt("fileName.extension", delimiter = " ", skiprows = 0, usecols = none, dtype = float)`

Write text to a file with `np.savetxt("fileName.extension", array, delimiter = " ", newline = "\n", header = " ", comments = " ")`.

















