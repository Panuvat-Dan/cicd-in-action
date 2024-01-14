import pandas as pd
from myapp import *

df = readdf()


def test_col_exists(df):
    cols = ['Name', 'Age']
    assert cols in df.column


def test_duplicate(df):
    assert df.duplicates() == True
