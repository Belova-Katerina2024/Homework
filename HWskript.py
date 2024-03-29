import pandas as pd

data = {'interval': [78.3,82.3,86.3,90.3,94.3,98.3,102.3,106.3], 
        'kol': [1,4,6,17,39,17,13,3]}

df = pd.DataFrame(data)
df

R= df_2.interval.max()-df_2.interval.min()