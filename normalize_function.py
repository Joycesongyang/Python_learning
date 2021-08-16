import numpy as  np 

def normalize(df, pd_series):
    pd_series = pd_series.astype(float)

    # Find upper and lower bounds for outliers
    avg = np.mean(pd_series)
    sd = np.std(pd_series)
    lower_bound = avg - 2 * sd
    upper_bound = avg + 2 * sd

    # Collapse in the outliers
    df.loc(pd_series < lower_bound, "cutoff_rate") = lower_bound
    df.loc(pd_series > upper_bound, "cufoff_rate") = upper_bound

    # Finally, use the log normalization
    normalized_price = np.log(df["cutoff_rate"].astype(float))

    return normalized_price
