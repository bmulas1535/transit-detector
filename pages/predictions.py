# Converter
def fits_convert(file):
    # Get astropy
    from astropy.io import fits

    # Retrieve BJD and PDCSAP from HDU header
    with fits.open(file, mode='readonly') as hdulist:
        k2_time = hdulist[1].data['TIME']
        pdcsap_fluxes = hdulist[1].data['PDCSAP_FLUX']

    import pandas as pd 

    # Create placeholder dataframe
    lightcurve = pd.DataFrame() 

    # Set columns
    for x in range(len(k2_time)):
        lightcurve[f'FLUX.{x}'] = 1
    
    # Fill with data from HDU
    lightcurve.loc[0] = pdcsap_fluxes

    # Drop nan
    lightcurve = lightcurve.dropna(axis=1)

    return lightcurve
# Transformer
def ft(x):
    y = spy.fft(x, n= x.size)
    return np.abs(y)

def transform_new(X):
    # Normalize the new data
    mean = X.sum(axis=1) / len(X.columns)
    X = X.subtract(mean, axis=0)
    X = pd.DataFrame(normalize(X))
    
    # Apply the FFT
    X = X.apply(ft, axis=1)
    
    # Re-format and split to correct length
    X = pd.DataFrame.from_records(X.iloc[[x for x in range(len(X))]])
    size = len(X.columns) - 1599
    X = X.loc[:,size:]
    
    # Provide uniform names for the column heads
    for i in range(len(X.columns)):
        X = X.rename(columns={X.columns[i]: f'f.{i+1}'})
        
    return X
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import base64
import io
import datetime
from dash.dependencies import Input, Output, State
from sklearn.preprocessing import normalize
import pandas as pd
import numpy as np 
import scipy as spy
import pickle

from app import app


column = dbc.Col([
    dcc.Markdown(
        """
        # Make a prediction!

        ### Upload a ```.fits``` file to detect transit signals
        """
    ),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select a File')
        ]),
        style={
            'width':'100%',
            'height':'60px',
            'lineHeight':'60px',
            'borderWidth':'1px',
            'borderStyle':'dashed',
            'borderRadius':'5px',
            'text-align':'center',
            'margin':'10px'
        }
    ),
    html.Hr(),
    html.Div(id='output-data-upload')
],
style={
    'text-align':'center'
},
md=12,
)

# Begin parse
def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        # Modified the example to integrate Brandon's code
        df = fits_convert(io.BytesIO(decoded))
        spec_data = transform_new(df)
        model = pickle.load(open('./assets/final_model.sav', 'rb'))
        prediction = model.predict_proba(spec_data)

    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    if prediction[0,1] > 0.01:
        return html.Div([
            html.H1(filename, style={'color':'#ededed'}),
            html.H2('Good candidate for transits!',
            style = {
                'color':'green'
            })
        ])
    else:
        return html.Div([
            html.H1(filename, style={'color':'#ededed'}),
            html.H2('No Transits.',
            style = {
                'color':'red'
            })
        ])

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(list_of_contents, list_of_names, list_of_dates)
        ]
        return children

layout = dbc.Row([column])