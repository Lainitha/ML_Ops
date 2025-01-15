import logging

import pandas as pd
from zenml import step

@step
def clean_df(df:pd.DataFrame:)-> None:
    """_summary_

    Args:
        df (_type_): _description_

    Returns:
        pd.DataFrame: _description_
    """
    pass
