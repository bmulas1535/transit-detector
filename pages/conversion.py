# Library to get data from fits file;

def fits_convert(file):
    # Get astropy
    from astropy.io import fits

    # Get location for the file
    DATA_PATH = "/"
    fits_file = (DATA_PATH + file)

    # Retrieve BJD and PDCSAP from HDU header
    with fits.open(fits_file, mode='readonly') as hdulist:
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