import plotly.figure_factory as ff
import pandas as pd

f = pd.read_csv('data/data.csv')
# f = f.groupby('Height(Inches)',)
hlist = list(map(lambda x: round(x*25.4)/10, f["Height(Inches)"].to_list()))
# print(hlist)
wlist = list(map(lambda x: round(x*4.53592)/10, f["Weight(Pounds)"].to_list()))
fig = ff.create_distplot([hlist, wlist], group_labels=[
                         'Height(Inches)', 'Weight(Pounds)'], show_hist=False)
fig.show()
