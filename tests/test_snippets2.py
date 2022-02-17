from snippets2 import utils
import pandas as pd
import pandas.testing
import pytest
from pathlib import Path
from os.path import join


@pytest.fixture
def iris():
    THIS_DIR = Path(__file__).parent
    file_path = join(THIS_DIR,'iris.csv')
    return pd.read_csv(file_path)

def test_csnapshot(iris):
    actual = (
        iris.
        pipe(utils.cfilter, lambda x: x.columns.str.contains("sepal"), axis="columns")
    )
    expected = iris.loc[:,['sepal_length',	'sepal_width']]

    pd.testing.assert_frame_equal(actual, expected)

@pytest.fixture
def test_df():
    THIS_DIR = Path(__file__).parent
    file_path = join(THIS_DIR,'test_df.csv')
    return pd.read_csv(file_path)
    
def test_df_to_code(test_df):
    actual = utils.df_to_code(test_df)
    expected = """pd.DataFrame ( {'test': {0: 1, 1: 2, 2: 3}, 'test1': {0: 4, 1: 5, 2: 6}} )"""
    assert actual == expected

@pytest.fixture
def teal_colour():
    return ("#0AD2A0")

def test_Colours(teal_colour):
    assert utils.Colours().oodle_teal == teal_colour