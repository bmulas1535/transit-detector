import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

### Create lightcurve plotly graph ###
from astropy.io import fits
import pandas as pd
import matplotlib.pyplot as plt
import numpy

DATA_PATH = 'assets/'
file = 'ktwo201092629-c102_llc.fits'

with fits.open(DATA_PATH + file, mode='readonly') as hdulist:
    k2_time = hdulist[1].data['TIME']
    pdcsap_fluxes = hdulist[1].data['PDCSAP_FLUX']

# Set up lightcurve in dataframe
lightcurve = pd.DataFrame()
for x in range(len(k2_time)):
    lightcurve[f'FLUX.{x}'] = 1

lightcurve.loc[0] = pdcsap_fluxes

lightcurve = lightcurve.dropna(axis=1)

# Plot it
lightcurve_plot = plt.figure()
plt.title('Interactive Lightcurve')

X = range(0, lightcurve.shape[1])
y = lightcurve

plt.scatter(X, y, s=1, alpha=0.7, color='black')

plt.xticks([0, 500, 1000, 1500, 2000],['','','','',''])
plt.xlabel('Time')

plt.yticks([262500, 263500, 264500, 265500, 266500], ['','','','','',''])
plt.ylabel('Flucuation')

plt.grid(True)

# Convert to plotly graph
from plotly.tools import mpl_to_plotly

plotly_figure = mpl_to_plotly(lightcurve_plot)

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

header = dbc.Col(
    [
        dcc.Markdown(
            """
            ![header](/assets/header.png)
            """
        ),
    ],
    md=12,
    style={
        'textAlign':'center',
    }
)

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predicting Transits

            Using raw `.fits` files, this app is able to convert space telescope data into readable
            lightcurves, and find the signals for planetary (or other) types of transits. \n

            If you can supply your own `.fits` file, the model can predict if it contains transit signals!
            """
        ),
        dcc.Link(dbc.Button('Try it now!', color='primary'), href='/predictions')
    ],
    md=5,
)

column2 = dbc.Col(
    [
        dcc.Graph(
            id = 'lightcurve-graph',
            figure = plotly_figure
        ),
        dcc.Markdown([
            """
            (Can you spot the transit?)
            """
        ], style={'textAlign':'center'})
    ],
    md=7,
)
layout = dbc.Row([header]),dbc.Row([column1, column2])
