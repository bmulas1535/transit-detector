import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

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
        dcc.Link(dbc.Button('Try it now!', color='secondary'), href='/predictions')
    ],
    md=5,
)

column2 = dbc.Col(
    [
        html.H3('What is a Transit?', style={'textAlign':'center'}),
        dcc.Markdown(
            """
            ![lc](assets/ex-transit.svg)
            """
        ),
    ],    
    md=7,
    style={
        'textAlign':'center',
    },
)

column3 = dbc.Col(
    [
        html.P(' ')
    ],
    md=5,
)

column4 = dbc.Col(
    [
        dcc.Markdown(
            """
            A transit is typically identified by a sharp decrease in observed star luminosity. By studying these graphs, one can observe visual indication of a planetary transit. The dips may be harder to spot, if the planet is relatively small, or if the star is very dim. Because of these factors, it's helpful to have a model that can clue you in on which lightcurves possibly have transits, and which don't!
            """
        )
    ],
    md=7,
)
layout = dbc.Row([header]),dbc.Row([column1, column2]), dbc.Row([column3, column4])
