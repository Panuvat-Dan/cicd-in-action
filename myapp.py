import pandas as pd
import pytest
print("Hello CICD")
# Extract Function


def readdf():
    data = [['tom', 10], ['nick', 15], ['juli', 14], ['tom', 10]]
    df = pd.DataFrame(data, columns=['Name', 'Age'])
    return df


df = readdf()
print(df.columns)
