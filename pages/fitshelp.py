import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import base64
import io
import datetime
from dash.dependencies import Input, Output, State

from app import app

head = dbc.Col(
    [
        dcc.Markdown(
            """
            # How to get a `.fits` file
            """
        ),
        html.Hr(),
    ],
    style={
        "textAlign":"center"
    },
    md=12,
)

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ###    Step 1 - Find the source

            `.fits` files are raw binary data compiled directly from space telescopes. There are a few sources on the net, but one of my favorites is the MAST database. You can access it for free, and use their file delievery system to download as many / whichever `.fits` files are available. You can find the database at:

            >[STSCI DATA ARCHIVE](https://archive.stsci.edu/missions/k2/lightcurves/) (recommended)

            You can also search the K2 missions by using the K2 mission search portal. That can be found at:

            >[K2 Search Portal](http://archive.stsci.edu/k2/data_search/search.php)





            ###    Step 2 - Download a file
            
            If you are using the **STSCI DATA ARCHIVE**, the process for finding a file to use is fairly straightforward. If you select any folder starting with `c_`, and follow any path through the next folderst that follow, and you will arrive at a `.fits` file! It really is that simple.
            
            If you're more experienced, and wish to collect more specific data, a brief tutorial covering how to do that will be provided in the annex at the bottom of this page.





            ###    Step 3 - Upload!

            Once you have downloaded the file, you simple need to visit the [Prediction](predictions.py) page, upload the file, and wait for your result! Congratulations! The model will now generate a prediction, and supply you with the End prediction, and some brief explaination.

            """
        ),
        html.Hr(),
    ],
)
column2 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Tutorial on the STSCI Database File Structure
            """
        ),
    ],
    style={
        "textAlign":"center",
    }
)
column3 = dbc.Col(
    [
        dcc.Markdown(
            """
            ### How it's set up - A brief tour

            The database has been designed for ease of finding the exact file, for the specific mission / campaign / time of your choosing. This makes it easier for you to track down the exact lightcurve that you're looking for. You can also use the **Search and Retrieve** (the second link) to search for a specific kind of lightcurve, using the database name to find in the Archive.

            ### The file-Structure

            When you enter the k2/lightcurves/ database, You will see several folders preceeded with `c_`. These are the campaigns. There are 18 total campaigns. Inside, the files are broken down by sections. If you would like more detailed information about the STSCI ARCHIVE DATABASE, you can reach out to me personally by e-mail, linked in the footer below. Thanks for using this app! Please feel free to send any comments or issues to me via any of my contact methods.
            """
        )
    ]
)
layout = dbc.Row([head]), dbc.Row([column1]), dbc.Row([column2]), dbc.Row([column3])