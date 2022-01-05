import pandas as pd

df = pd.read_csv("/home/ca-ai/master_ws/map_data/src/mapa.txt", sep = ",")

print(df)

# Works but takes a while to print the pandas dataframe
# Will attempt to improve runtime
# Note: VS Code still highlights the line reading from pandas but does not cause the code to not work
# As you can see below in the terminal pandas is reading the mapa.txt in a weird way by adding decimals to the negative ones in the data
# Will fix tomorrow