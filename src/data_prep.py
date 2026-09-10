import pandas as pd

def wrangle_data(df_path):
    """
    Wrangle and preprocess the air quality dataset

    Args:
        df_path (Path or str): the path of the CSV dataset file
    Returns:
        pandas.Series: A cleaned and indexed PM2.5 (P2) time series
        ready for ARMA/ARIMA modeling.     
    """
    
    df = pd.read_csv(df_path, sep=";", header=None, low_memory=False)
    df.columns = [
    "sensor_id", "sensor_type", "location",
    "lat", "lon", "timestamp",
    "value_type", "value"
    ]
    # dropping the duplicated column names and resetting the index
    df = df.drop(df.index[0])
    df = df.reset_index(drop=True)
    
    # mask for the PM2.5 readings
    p2_mask = df["value_type"]== "P2"
    
    # mask for tha location "7"
    loc_7_mask = df["location"]=="7"
    
    df = df[p2_mask & loc_7_mask]
    
    df = df[["timestamp", "value"]]
    df = df.set_index("timestamp")
    
    # convert index to a datetime index
    df.index = pd.to_datetime(df.index)
    
    # converting the time zone to Africa/Nairobi local time
    df.index = df.index.tz_convert("Africa/Nairobi")
    
    # convert the value of reading to float
    df["value"] = df["value"].astype("float")
    
    # rename the value columns to P2
    df = df.rename(columns={"value":"P2"})
    
    # Dealing with out liers
    low,high = df["P2"].quantile([0.0, 0.95])
    df =  df[df["P2"].between(low,high)]
    
    # resample the data to "1h"
    df = df["P2"].resample("1h").mean().ffill().to_frame()
        
    return df
    
    