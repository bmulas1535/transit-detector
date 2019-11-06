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

            ## Creating an exoplanet transit detector
            ----------


            """
        ),

    ],
    className="d-flex justify-content-center",
    md=12,
)

column2 = dbc.Col(
    [
        html.Div([
            html.Img(
                src='../assets/spec1.png',
            ),
        ],
        className="float-right",
        style={
            "marginLeft":"10px"
        }
        ),
        html.Div([
            html.H4(
                """Organizing the data"""
            ),
            html.P(
                """
                The first step in every Data Science adventure, I imagine,
                is collecting the data. I've always had an interest in 
                Astrophysics, so when I found I needed data to work with,
                I decided to try and find something in this field. I settled
                on a Kaggle dataset I found using star luminosity. The data 
                came nicely packaged, but that in itself would later create
                problems. And so, I set out to predict exo-planet transits in
                lightcurve data!
                """
            ),
            html.H4(
                """A format for a model"""
            ),
            html.P(
                """
                As I am sure most are aware, not all formats are created
                equal. Before I could choose definitively in what shape
                I would present data to my model, I had to decide on a 
                model to use. Knowing how a model uses data is key, especially
                if what you're trying to predict isn't as tangable as 
                sale prices or success rates. 
                """
            ),
            html.P(
                """
                It was apparent that this data needed to be treated
                differently. To get the most out of the lightcurve
                data, I needed a method to remove guesswork from the back of
                any model that I chose. As I was contemplating ways of 
                reducing the complexity of the data by calculating "time
                delta", it occured to me that someone had already done this 
                for frequency data. As it happened, I was sitting with 
                just that kind of data, and so I used the Forward Fourier
                Transform to translate the raw luminosity data into
                a frequency spectrum.
                """
            ),
            html.P(
                """
                The next step was to ensure that not only was all of the 
                required information translated and presentable to a model,
                but also to ensure that unnessessary complexity had been
                removed from that data. The calculations were already looking
                to be intense with over 3000 columns in my dataframe.
                Any reduction
                was certainly warranted. Upon plotting the spectrum data, I
                found that the spectra were symmetrical, as expected. By
                cutting them in half, essentially, I was able to reduce the 
                amount of raw data consumed by my future model by 50%.
                """
            ),
            html.P(
                """
                As a caveat, is should be noted that splitting the data this
                way has no effect other than to reduce the total
                computation time for a model. This was confirmed by passing
                the raw spectrum data through a seperate model, which
                was not able to outperform. The only concievable reason
                to leave the spectra raw would be to take a longer amount
                of time to calculate the same answer. This, as the antithesis
                of efficient, was not the desired course of action.
                """
            ),
        ]),
        html.Div([
            html.Img(
                src="../assets/auprc.png"
            )
        ],
        className="float-left d-flex",
        style={
            "paddingRight":"10px"
        }),

        html.Div([
            html.H4(
                """
                To train a model
                """
            ),
            html.P(
                """
                At this point, the data has been processed and transformed as
                much as I could concieve was warranted. The only task that
                remained was to pick a baseline model to use. Chief amoung 
                the considerations for which model to use was effciency.
                In the end, the decision was a toss up between a ridge
                logistic classifier and a tree based classifier. In the end,
                I decided to try out the tree based classifiers to see how
                they would fare with this data.
                """
            ),
            html.P(
                """
                For the baseline, I used a 7 layter tree random forest,
                from the sci-kit learn library. It did about as well as
                I could expect, considering the imbalanced classes and lack
                of any real guidance. It scored about 58 percent accracy,
                with approximately 1 percent recall. Not so good.
                """
            ),
            html.P(
                """
                It would seem that the XGBoost Classifier would be the better
                option. Being able to build new trees with prior knowledge
                would help the model learn more from the data available. The
                remaining problem, namely imbalanced classes, was solved by
                oversampling the positive class using SMOTE.
                """
            ),
            html.P(
                """
                With these methods, the prevailing model was able to achieve
                a 68 percent Area under Precision Recall curve score. Not bad!
                The real key, however, was going to be how well this model
                was identifying the right frequencies. The question was posed,
                "How important was each frequency?"
                """
            )
        ]),

        html.Div([
            html.Img(
                src="../assets/feat_import.png"
            )
        ],
        className="d-flex float-right",
        style={
            "paddingLeft":"10px"
        }),

        html.Div([
            dcc.Markdown(
                """
                #### Finding the sweet spot

                When building a model, we generally want the model
                to be as accurate as we can make it. It's important,
                however, not to be overzealous. Easier than striking the
                perfect balance is accidently tipping the scales in the
                search for that high accuracy score metric. In the case
                of the model at hand, I appeared to have struck just
                the balance that I sought.
                """
            ),
            dcc.Markdown(
                """
                #### Modifying the Threshold

                The first run of this model on my test data did not look very
                promising! An accuracy score of just above 58 percent, and
                horrible recall. Upon investigation of feature importance, I
                found something incredible. The tree based classifier was not
                very confident about which lightcurves had transits. It was,
                however, very confident about which ones did not! I set up a
                graph for feature importance and found that very few of the 
                1599 frequencies were considered with greater than
                1 percent of importance. This was great news! Now I understood
                that in order to achieve my goal of perfect recall, I simply
                needed to ask my model for which lightcurves it wasn't
                sure **DID NOT** have transits! By changing the positive
                prediction threshold from 0.5 to 0.01, I lost some in the
                way of raw accuracy (added quite a few more false positives),
                but inspired a model that correctly caught all known
                transits.
                """
            )
        ]),
        html.Div([
            html.Img(
                src="../assets/cm.png"
            )
        ],
        className="d-flex float-left",
        style={
            "paddingRight":"10px"
        }),
        html.Div([
            dcc.Markdown(
                """
                #### Cost / Benefit Analysis

                At the end of the day, or project in this case, It is
                imperative that the result of our efforts have produced
                a product that is viable and has benefits that outweigh
                the costs of it's implementation. I will need to examine
                and confirm that this app would save time or money as 
                compared to the baseline methods. Assuming the baseline
                is inspecting each lightcurve by hand (no easy feat),
                our model shines! with near 90 percent of negatives 
                accurately classified, we only have to contend with 
                approximately 10 percent of the population as false
                positives. 

                I have analyzed lightcurves by hand in the past, and will
                endevor to add perspective to my argument that this is much
                more efficient than looking at each one by hand. Many 
                transit signals are very difficult to spot, and are 
                only detected via mathematical signals. Therefore, each
                lightcurve must be subjects to severals rounds of complex
                equations to determine if a transit is present. This process
                can sometimes take hours, and even then the results must
                be reviewed by multiple researchers to ensure accuracy of
                classification. While those sorts of checks must always be
                present, we can eliminate a lot of overhead time and effort
                and potentially money, by raising our level of confidence in
                each classification. Less time on each set of data is more 
                time finding positive transits.
                """
            )
        ])
    ]
)


layout = (
    dbc.Row(
        [column1]
    ),
    dbc.Row(
        [column2]
    )
)
