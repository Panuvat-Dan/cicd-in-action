import pandas as pd
from myapp import *


@pytest.fixture
def readdf():
    data = [['tom', 10], ['nick', 15], ['juli', 14], ['tom', 10]]
    df = pd.DataFrame(data, columns=['Name', 'Age'])
    return df

def test_col_exists(df):
    cols = ['Name', 'Age']
    assert cols in df.column


def test_duplicate(df):
    assert df.duplicates() == True
