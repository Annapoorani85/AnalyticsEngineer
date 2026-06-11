import pandas as pd
import os
from deltalake import DeltaTable
from deltalake.writer import write_deltalake

df = pd.DataFrame({"x": [1, 2, 3]})
print("DataFrame created:")
print(df)

write_deltalake("data", df)
print("Data written to Delta Lake successfully!")