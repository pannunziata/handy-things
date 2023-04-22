from ipywidgets import *

header = HTML("<h1 style=color:white;>Paul's Application</h1>", layout=Layout(height='auto'))
paul = HTML("<h1 style=color:white;>TEST</h1>", layout=Layout(height='auto'))
test = HTML("<h1 style=color:white;>TEST</h1>", layout=Layout(height='auto'))
text = HTML("<h3 style=color:white;>this is application i have coded to play around with how making a better looking app for data quality will look</h3>", layout=Layout(height='auto'))


AppLayout(
    header=header,
    left_sidebar=VBox([text]),
    right_sidebar=VBox([test]))