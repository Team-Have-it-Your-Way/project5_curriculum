import pandas as pd
import numpy as np

def acquire_df():
    '''
    Acquires and returns the curriculum access data.

    Returns:
    -------
    pandas.DataFrame:
        A DataFrame containing the curriculum access data with columns: 'dates', 'time', 'endpoint', 'user_id',
        'cohort', and 'ip'.
    '''
    # read csv
    df = pd.read_csv("anonymized-curriculum-access.txt", sep=" ", header=None)
    # rename columns
    df.columns = ["dates", "time", "endpoint", "user_id", "cohort", 'ip']
    return df

def prepare_df():
    """
    Prepare the DataFrame by handling nulls, merging tables, dropping columns, and updating data types.
    
    Returns:
    df (DataFrame): Prepared DataFrame after performing necessary transformations.
    """
    # read df
    df = acquire_df()
    # ----handle nulls
    # change cohort nulls to 0
    df.cohort = df.cohort.fillna(0)
    
    

    # drop 1 null in endpoint
    df = df.dropna()

    # Remove '\t\t' character from col1
    df.dates = df.dates.str.replace("\t\t", "")
    

    # read cohort df
    cohort_df = pd.read_csv("curriculum_logs_cohorts.csv")
    
    # ----- merge tables
    # rename id to cohort to match
    cohort_df = cohort_df.rename(columns = {"id": "cohort"})

    # merge on cohort
    df = pd.merge(cohort_df, df,  on=['cohort'], how='right')

    # drop columns
    df = df.drop(columns=[ 'slack',  'created_at', 'updated_at', 'deleted_at'])

    # update dtype for dates to datetime64
    df.start_date = df.start_date.astype("datetime64")
    df.end_date = df.end_date.astype("datetime64")
    df.dates = df.dates.astype("datetime64")

    # rename columns
    df = df.rename(columns = {"cohort": "cohort_id", "name": "cohort_name"})

    return df  
   
