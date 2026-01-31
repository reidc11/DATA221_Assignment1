#Caitlin Reid|30245427   DATA 221 Assignment 1
# Question 8: Pandas DataFrame with Computed Column
# Install the pandas package and import it using the alias pd. Then:
# • Create a DataFrame using the provided column data.
# • Add a new column derived from existing columns.
# • Print the final DataFrame.

#Done

import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B":[3.1, 4.2, 1.5, 6.3,],
    "C": [800, 150, 400, 210]
}

dataFrame = pd.DataFrame(data)

dataFrame["D"] = dataFrame["A"] * dataFrame["B"] + dataFrame["C"]

print (dataFrame)