# Exoplanet Transit Detector

![lc](assets/header.png)

### Details

The model was trained on ~5000 rows of data from the 3rd campaign of the K2 mission. It uses a
classification algorithm to detect probability of a transit. Currently, the model is able to produce:

* 100% TP
* 89.6% TN
* 10.4% FP
* 0% FN

### Model

Currently, the model used to classify exo-planet transits in this app is the XGBoost Classifier. This model was chosen due to the need for recursive building of new trees with prior knowledge. Because the data contains so few positive classes, the few positives that do exist were oversampled, and the model is used specifically to identify **non-transit** systems, with a positive class indicated by just 1% probability of a transit.

---------------------
The app is hosted [here](https://transit-detection.herokuapp.com) using **Heroku**. Please allow up to 1 minute for the app to "wake up".
