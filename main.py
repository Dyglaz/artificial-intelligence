import numpy as np
import pandas as pd


a = pd.Series([2, 4, 3, -10])
b = pd.Series([-2, 1, 6, 1])
print(a, b, sep='\n')
print("Distance:", sum((a - b)**2)**0.5)
