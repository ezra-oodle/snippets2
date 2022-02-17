import pandas as pd
import numpy as np
from typing import Union

def show_all_columns(df):
    # I dont think this is working
    """Set and then reset max column width"""
    pd.set_option('display.max_columns', None)
    try:
        return df
    finally:
        pd.reset_option("max_columns")

def csnapshot(df: pd.DataFrame, fn = lambda x : x.shape, msg = None) -> pd.DataFrame:
    """
    Custom help function to print out things during method chaining
    Inputs a df and outputs a df. 
    """
    if msg:
        print(msg)
    display(fn(df))
    return df

def setcols(df, fn=lambda x: x.columns.map('_'.join), cols=None):
    """Sets the column of the dataframe to the passed column list.

    """
    if cols:
        df.columns = cols
    else:
        df.columns = fn(df)
    return df

def cfilter(df, fn, axis="rows"):
    """ Custom Filters based on a condition and returns the df.
        function - a lambda function that returns a binary vector
        thats similar in shape to the dataframe
        axis = rows or columns to be filtered.
        A single level indexing
        
        (
            iris.pipe(
            setcols,
            fn=lambda x: x.columns.str.lower()
            .str.replace(r"\(cm\)", "")
            .str.strip()
            .str.replace(" ", "_"),
            ).pipe(cfilter, lambda x: x.columns.str.contains("sepal"), axis="columns")
        )
    """
    if axis == "rows":
        return df[fn(df)]
    elif axis == "columns":
        return df.iloc[:, fn(df)]



#Get the nones in each col
def filter_out_none_cols(df,threshold = 500):
    """Looks for the number of 'None's in each column, filters out the column is there is graet number than the threshold"""
    good_cols = df.columns[ np.sum(df=='None',axis= 0) < threshold ]
    return df.loc[:,good_cols]
    

def df_to_code(df):
    """
    Returns a string that defines to df, used for producing minimal reporoducable examples
    or simple dfs to be used in unit testing.
    eval(df_string) could be used to evaluate the string, or copy paste into code. 
    """
    df_string = ( f"pd.DataFrame ( { str( df.to_dict() ) } )")
    return(df_string)


def csv_string_to_df(input_string):
    """
    Produce a df from a csv string
    """
    df_from_String = pd.DataFrame(
    [x.split(',') for x in input_string.split('\n')[1:]],
    columns=input_string.split('\n')[0].split(",")
    )
    return(df_from_String)

def test_func():
    print("woo, orkig!")

def print_df_dims(df: pd.DataFrame,df_rows: int) -> None:
    """Print formatted row and column dimensions of a dataframe"""
    percent_of_total = round(100*(df.shape[0]/df_rows ),3)
    print(
        f"Rows: {df.shape[0]} ({percent_of_total}% of full dataframe)\nColumns: {df.shape[1]}"
    )


def value_counts_v2(s: Union[pd.Series, pd.DataFrame]) -> pd.DataFrame:
    """
    Returns that normalised and unnormalised columns in value_counts()
    Useful when you want to know absoluoute number any percentage
    """

    if isinstance(s, pd.Series):
        s = s.to_frame()

    df = s.value_counts(normalize=False, dropna=False).reset_index()
    df.columns = list(df.columns[0:-1]) + ["n"]
    df = df.assign(p=lambda df: df.n / sum(df.n))
    return df