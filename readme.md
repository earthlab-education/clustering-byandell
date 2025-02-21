# Assignment ea-02-clustering

This repository contains the notebooks for this week's assignment. 
See
[2. Clustering: Land cover classification at the Mississippi Delta](https://cu-esiil-edu.github.io/esiil-learning-portal/foundations/notebooks/12-clustering/clustering.html).

Complete
the homework in each .ipynb notebook, commit your work, and push the changes
to github. Your instructor will pull the completed assignment after the
deadline.

Once grading is complete, your instructor will push the results to a file
called `feedback.html`. You will need to pull the changes to your local copy
and open this file in a browser to view (because GitHub will not render html 
files).

Notes for next assignment on 
[classes](https://docs.python.org/3/tutorial/classes.html).
A class is a function with output of an object that has new methods, which are in turn functions
defined in the class.
In addition, the `@property` decorator defines attributes for the object.

- [apppeears.py](https://github.com/earthlab/earthpy/blob/apppears/earthpy/appeears.py)
- add functionality to class
- diff functions with same parameter--streamline, keep track of metadata

```
import **stuff**

class ArrayDataFrame(pd.DataFrame): # inherits pd.DataFrame class

    def set_array_column(self, arrays):
        self['arrays'] = arrays
        return self

    def __repr__(self):
        for_printing = self.copy()
        for_printing.arrays = [arr.min() for arr in self.arrays]
        return for_printing.__repr__()
        

ArrayDataFrame({'url': ['https://...']}).set_array_column([xr.DataArray()])

# Slow example where class would help.
import random
import numpy as np

def gen_data_array(size=10):
    data = (
        np.array([random.gauss(0,1) for _ in range(size**2)]).reshape(size, size))
    data = xr.DataArray(
        data = data,
        coords = (
            'x': [i * random.uniform(0,1) for i in range(size)],
            'y': [i * random.uniform(0,1) for i in range(size)],
        )
    )
    return da

df_len = 10
md_df = pd.DataFrame([
    'id': list(range(df_len)),
    'array': [gen_data_array(10) for _ in range(df_len)]])
my_df
```

```
class FunDataFrame(pd.DataFrame):

    def __repr__(self):
    return 'stuff!'

md_df = FunDataFrame([
    'id': list(range(df_len)),
    'array': [gen_data_array(10) for _ in range(df_len)]])
my_df

# Add ipython method (under the hood)

class FunDataFrame(pd.DataFrame):

    def __repr__(self):
    return 'stuff!'

    def _repr_html_(self):
        return 'more stuff!!!'

md_df = FunDataFrame([
    'id': list(range(df_len)),
    'array': [gen_data_array(10) for _ in range(df_len)]])
my_df

# Set up my dataframe class to show what I want

class FunDataFrame(pd.DataFrame):

    # tell it what I define
    array_types = [xr.DataArray]

    # make array as a property
    @property
    def array_cols(self):
        array_cols = []
        for col in self:
            if type(self[col][0]) == xr.DataArray:
                array_cols.append(col)
                return array_cols
            

    @property
    def _df_for_repr_(self):
        df = self.drop(columns = self.array_cols).copy()
        for array_col in self.array_cols:
            arr_str_list = []
            for arr in self[array_col]:
                arr_min = round(float(arr.x.min()), 2)
                arr_max = round(float(arr.x.max()), 2)
                arr_str_list.append(
                    f'DataArray(x ({arr_min}, {arr_max}))'
                )
            df[array_col] = arr_str_list
            #df[array_col] = ['DataArray' for _ in range(len(df))]
        return df
    
    # represent
    def __repr__(self):
        return self._df_for_repr_.__repr__()'

    # ipython method
    def _repr_html_(self):
        return self._df_for_repr_._repr_html_()

md_df = FunDataFrame([
    'id': list(range(df_len)),
    'array': [gen_data_array(10) for _ in range(df_len)]],
    'array2': [gen_data_array(10) for _ in range(df_len)]])
my_df
```

