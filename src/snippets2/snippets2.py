
def csnapshot(df, fn = lambda x : x.shape, msg = None):
    """
    Custom help function to print out things during method chaining
    Inputs a df and outputs a df. 
    """
    if msg:
        print(msg)
    display(fn(df))
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


class Colours:
    
    # Primary Palette
    oodle_teal = '#0AD2A0'
    oodle_navy = '#312F43'
    oodle_white = '#FFFFFF'

    # Secondary Palette
    oodle_pink = '#EC608A'
    oodle_orange = '#FB9F1E'
    oodle_purple = '#6059A3'


    def __init__(self):
        pass
    


def test():
    print('Haray, it worked')