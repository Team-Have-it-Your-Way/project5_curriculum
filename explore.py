#################### imports

# standard imports
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import seaborn as sns

# tools imports
import matplotlib.pyplot as plt

# functions .py imports
import wrangle as w

#################### functions

def get_program_id_df(df):
    '''take in prepared df and creates three df's for each program WebDev, DataScience'''
    
    # make dataframes for each program
    df1 = df[df['program_id'] == 1.0]
    df2 = df[df['program_id'] == 2.0]
    df3 = df[df['program_id'] == 3.0]
    
    return df1, df2, df3

def plot_endpoints_counts(df, endpoint_string):
    '''group by cohort_id and count the number of occurrences of the string in endpoint column and plot the counts as a bar chart'''
    
    # group by cohort_id and count the number of occurrences of the string in endpoint column
    counts = df.groupby('cohort_id')['endpoint'].apply(lambda x: x.str.contains(endpoint_string).sum())

    # plot the counts as a bar chart
    ax = counts.plot(kind='bar', figsize=(10, 6), color='blue', alpha=0.5)

    # set the chart title, x-axis label, and y-axis label
    ax.set_title(f'Number of Occurrences of Endpoint with String\n "{endpoint_string}" by Cohort', fontsize=14)
    ax.set_xlabel('Cohort ID', fontsize=12)
    ax.set_ylabel('Number of Occurrences', fontsize=12)

    # show the plot
    plt.show()
    
def plot_endpoints_ds(df3):
    '''graph all three lessons broken down by cohorts and compare side by side'''

    # group by cohort_id and count the number of occurrences of the string in endpoint column for each string
    counts1 = df3.groupby('cohort_id')['endpoint'].apply(lambda x: x.str.contains('classification/overview').sum())
    counts2 = df3.groupby('cohort_id')['endpoint'].apply(lambda x: x.str.contains('1-fundamentals/1.1-intro-to-data-science').sum())
    counts3 = df3.groupby('cohort_id')['endpoint'].apply(lambda x: x.str.contains('sql/mysql-overview').sum())

    # create a figure and axes object
    fig, ax = plt.subplots(figsize=(10, 6))

    # plot each count as a bar chart with a different color
    counts1.plot(kind='bar', ax=ax, color='blue', alpha=0.5, position=0, width=0.25)
    counts2.plot(kind='bar', ax=ax, color='red', alpha=0.5, position=1, width=0.25)
    counts3.plot(kind='bar', ax=ax, color='green', alpha=0.5, position=2, width=0.25)

    # set the chart title, x-axis label, and y-axis label
    ax.set_title('Number of Occurrences of Endpoint with Different Lessons by Cohort', fontsize=14)
    ax.set_xlabel('Cohort ID', fontsize=12)
    ax.set_ylabel('Number of Occurrences', fontsize=12)

    # add a legend to the plot
    ax.legend(['classification/overview', '1-fundamentals/1.1-intro-to-data-science', 'sql/mysql-overview'])

    # show the plot
    plt.show()
    