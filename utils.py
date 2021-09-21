import pandas as pd
import numpy as np

def convert_to_multiindex(df):
    df = df.groupby(level=0).apply(lambda x: x.set_index('date').resample('1M').last())
    df = df.reset_index()
    df = df.set_index(['date','ticker']).sort_index()
    return df