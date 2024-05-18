import numpy as np
import pandas as pd
arr = [21, 10,15, 20, 8, 13, 4,  10, 12, 25]

#nd_arr = np.array(arr)
sr = pd.Series(arr)
mean = sr.mean()
median = sr.medain()
mode = sr.mode()
