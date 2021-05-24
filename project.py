import plotly.figure_factory as ff
import pandas as pd

print("Reading Data")
f = pd.read_csv('data/project.csv')
# fig =ff.create_distplot([f["Mobile Brand"].to_list(),f["Avg Rating"].to_list()],group_labels=["Mobile Brand","Avg Rating"])
print("Creating plot...")
fig =ff.create_distplot([f["Avg Rating"].to_list()],group_labels=["Avg Rating"])
print("Displaying plot...")
fig.show()
