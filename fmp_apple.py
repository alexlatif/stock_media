from urllib.request import urlopen
import json
import pandas as pd

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


url = ("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?apikey=649ce3d54d0f5c0679f710b5d2f7ac95")
data = get_jsonparsed_data(url)
df = pd.DataFrame.from_dict(data)
df.to_csv('apple_stock.csv', ',')
