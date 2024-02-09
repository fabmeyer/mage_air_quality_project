import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte/download/ugz_ogd_air_h1_2024.csv'
    response = requests.get(url)

    dtypes = {
        'Standort': str,
        'Parameter': str,
        'Intervall': str,
        'Einheit': str,
        'Wert': float,
        'Status': str
    }

    parse_dates = ['Datum']

    return pd.read_csv(url, sep=",", dtype=dtypes, parse_dates=parse_dates)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
