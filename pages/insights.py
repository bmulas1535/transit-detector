import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## -- The Model --

            ### What is the model doing?

            This model was designed to take in raw binary data that the telescopes produce. It then compares this spectrum, and gives a predcition about how closely it resembles a **non-transit** spectrum.

            ### How is the model useful?

            There is a lot of work still being done in the detection and identification of Exoplanets! This type of model would be able to assist researches in cutting back the time spent sifting through mountains of lightcurves looking for the handful that have transits! Out of every 15,000 stars, about 30 to 40 have detectable transits. That's a lot of data, and it's almost insurmountable without a way of excluding a big chunk of the negatives.

            """
        ),
        html.Hr(),
        dcc.Markdown(
            """
            ## -- Lightcurves --

            ### What is a lightcurve?

            A lightcurve is generated over time, as a telescope captures the light emitted by a start across several wavelengths. By combining certain data associated with the star, it is able to compile data representing the change in luminosity over the period it was observed. When you scatter plot that data, it is called a lightcurve.

            ### What can a lightcurve tell you?

            Short answer: A lot! Longer answer: There is an enormous amount of information about a star and it's solar system in lightcurve data. Aside from planet transits, you can also see star spot activity, eclipsing binary star systems, pulsars, black holes, comet swarms, and so much more! This data is a treasure trove of astronomic information.

            ### How many are there?

            In campaign 3 of K2, there were over 15,000 individual stars observed over a period of ~80 days. There have been approximately 18 campaigns in the K2 mission. K2 is one of many star observing missions, along with the likes of the Kepler mission, TESS, and soon the James Webb (launching soon!). We've recorded this data on hundreds of thousands of stars! That means we've looked at about less than 1 percent of our own galaxy, estimated at around 250 billion stars.

            ### If the curve doesn't indicate a Transit, does that mean the star has no planets?

            No! Unfortunately, the conditions for recording a transit have to be perfect, which doesn't always happen. The planet also needs to be sufficiently large to block out enough light from the host start to make an impact to the observer (us). If the planet's orbit does not intersect our line of sight, we won't be able to see it. If the planet's orbit takes longer than the observation period, we also will not detect it. That's why constant observation is key! This is only one of many tools we can use to detect Exoplanets.
            """
        )
    ],
    md=12,
)


layout = dbc.Row([column1])