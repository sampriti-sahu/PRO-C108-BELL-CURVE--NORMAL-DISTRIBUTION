import random
# import plotly.express as px
import plotly.figure_factory as ff

print("Running main.py")
sums = []
count =[]
for i in range(0,100):
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    sum1 = r1+r2
    sums.append(sum1)
    count.append(i)
    # print("{},{} sum:{}".format(r1, r2, sum1))
print(sums)
# sumf = pd.array(sums,x="result",y="count")
fig = ff.create_distplot([sums],group_labels=["sums"])

fig.show()