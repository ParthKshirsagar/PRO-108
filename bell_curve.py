import pandas as pd
import plotly.figure_factory as ff

file = 'data.csv'

df = pd.read_csv(file)

fig = ff.create_distplot([df['Avg Rating']], ['Average Rating'])

fig.show()