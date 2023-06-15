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
    
# ------------------- Question 3

def specify_staff(df, staff_list):
    """
    Specifies staff members in a DataFrame based on a given staff list.

    Args:
        df (pandas.DataFrame): The DataFrame to modify.
        staff_list (list): A list of user IDs representing staff members.

    Returns:
        pandas.DataFrame: The modified DataFrame with a new 'staff' column indicating staff membership.
    """
    df['staff'] = df['user_id'].apply(lambda x: 1 if x in staff_list else 0)
    return df

# accesses within cohort
def specify_timeframe(df, date, start_date, end_date):
    """Specify the timeframe for a DataFrame based on given dates.

    Args:
        df (DataFrame): The input DataFrame.
        date (str): The name of the column representing the dates to compare.
        start_date (str): The name of the column representing the start date of the timeframe.
        end_date (str): The name of the column representing the end date of the timeframe.

    Returns:
        DataFrame: The modified DataFrame with an additional column 'outside_cohort' indicating whether each row's date is outside the specified timeframe.
    """
    df['outside_cohort'] = df.apply(lambda row: 1 if row[date] < row[start_date] or row[date] > row[end_date] else 0, axis=1)
    return df

def categorize_field(data, field_name):
    """
    Categorizes values in a specified column of a DataFrame based on predefined categories.

    Args:
        data (pandas.DataFrame): The DataFrame containing the data.
        field_name (str): The name of the column to categorize.

    Returns:
        pandas.DataFrame: The modified DataFrame with an additional 'program_name' column.

    Raises:
        KeyError: If the specified column is not found in the DataFrame.
    """
    if field_name not in data.columns:
        raise KeyError(f"Column '{field_name}' not found in DataFrame.")
    
    categories = {
        1: 'Web Development 1.0',
        2: 'Web Development 2.0',
        3: 'Data Science'
    }
    
    def categorize(value):
        return categories.get(value, 'Unknown')
    
    data['program_name'] = data[field_name].apply(categorize)
    return data


def q3(df):
    """
    Filters the given DataFrame based on specific conditions and returns a DataFrame containing
    information about students who did not access the curriculum during their cohort.

    Args:
        df (pandas.DataFrame): The input DataFrame containing student data.

    Returns:
        pandas.DataFrame: A DataFrame with columns 'program_name', 'program_id', and 'user_id' 
        representing the program details and user IDs of students who did not access the curriculum 
        during their cohort.
    """
    # staff_list
    staff_list = [ 53, 314,  40,  64,  11, 211,   1, 312, 146, 248, 370, 397, 404,
       257, 428, 461,  37, 514, 539, 545, 546, 572, 315,  41, 592, 618,
       620, 521, 652, 502, 653, 480, 738, 742, 745, 813, 430, 816, 581,
       854, 855, 744, 893, 148, 894, 513, 630, 308, 951, 953, 980]
    
    df = specify_staff(df, staff_list)

    # whether they accesed during their cohort
    df = specify_timeframe(df, "dates", "start_date", "end_date")

    # list of student ids  
    students = df[df.staff == 0]
    student_ids = list(students.user_id.unique())

    # students who accessed curriculum outside cohort: 86900 times and 541 students
    student_accessed_outside_cohort = students[students.outside_cohort == 1]

    # students who accessed curriculum during cohort: 692348 times and 790 students
    student_accessed_during_cohort = students[students.outside_cohort == 0]

    access_curr = list(student_accessed_during_cohort.user_id.unique())

    # list of student user ids that did not access curriculum during cohort
    not_access_curr = [num for num in student_ids if num not in access_curr]

    # students that did not access curriculum within cohort 
    stu_not_access_curr_df = students[students['user_id'].isin(not_access_curr)]


    stu_not_access_curr_df = categorize_field(stu_not_access_curr_df, "program_id")
    stu_nac_df = stu_not_access_curr_df[["program_name", "program_id", "user_id"]].drop_duplicates()

    return stu_nac_df


def trim_legend(df, column_name, categories):
    """
    Trims and categorizes a column in a pandas DataFrame based on provided categories.

    Args:
        df (pandas.DataFrame): The DataFrame containing the column to be trimmed and categorized.
        column_name (str): The name of the column to be trimmed and categorized.
        categories (list): A list of categories to be used for categorization. Any values not
            matching the provided categories will be categorized as 'Other'.

    Returns:
        pandas.DataFrame: The modified DataFrame with the trimmed and categorized column.

    """
    categorized_column = df[column_name].apply(lambda x: x.strip() if isinstance(x, str) else x)
    categorized_column = categorized_column.apply(lambda x: x if x in categories else 'Other')
    df[column_name] = categorized_column
    return df


def plot_stacked_bar(df,yaxis,legend,title,xlabel,ylabel,limit=0,legendnames=None,figsize=None, palette="Pastel1"):
    """
    Generates a stacked horizontal bar plot based on the given DataFrame and parameters.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data to be plotted.
        legend (str): The column name in the DataFrame representing the legend/category.
        limit (int): The maximum number of categories to include in the plot. If there are more categories than the limit,
            the excess categories will be grouped under the "Other" category.
        yaxis (str): The column name in the DataFrame representing the y-axis values.
        palette (str or list): The color palette to use for the plot. It can be a named seaborn palette or a list of colors.
        figsize (tuple): The figure size (width, height) of the plot.
        legendnames (list or None): Optional. The list of legend/category names to use for labeling the plot legend.
            If None, the unique values from the 'legend' column will be used.
        title (str or None): Optional. The title of the plot. If None, no title will be displayed.
        ylabel (str or None): Optional. The label for the y-axis. If None, no label will be displayed.
        xlabel (str or None): Optional. The label for the x-axis. If None, no label will be displayed.

    Returns:
        None: The plot is displayed using matplotlib.pyplot.show().
    """
    lvalues = df.loc[:,legend]
    if limit > 0 and limit < len(lvalues.unique()):
        lvcounts = lvalues.value_counts().reset_index()
        lcats =  list(lvcounts.loc[:,'index'][:limit])
        df = trim_legend(df,legend,lcats)
        lcats.append("Other")
    else:
        lcats = list(lvalues.value_counts().reset_index().loc[:,'index'].unique())

    ycats = df.loc[:,yaxis].sort_values(ascending=False).unique()
    myOrd = df.loc[:,legend].replace({k: v for v, k in enumerate(lcats)})
    myOrd.value_counts()
    data= {}
    for ndx in range(0,len(ycats)):
        data[ycats[ndx]]= myOrd[df.loc[:,yaxis] == ycats[ndx]].dropna().value_counts()

    sns.set_palette(palette)
    plotdata = pd.DataFrame(data).T
#     plotdata = Tpose.div(Tpose.sum(axis=1), axis=0) * 100

    plotdata.plot(kind='barh',figsize=figsize, stacked=True)
    plt.legend((lcats,legendnames)[legendnames!=None], bbox_to_anchor=(1.05, 1)).remove()
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()


# ------------------- Question 6 & 7
def saoc_df(df):
    '''
    Filter the DataFrame to return students who accessed outside their cohort.

    Parameters:
        df (pandas.DataFrame): The input DataFrame containing student data.

    Returns:
        pandas.DataFrame: A DataFrame containing students who accessed outside their cohort.
    '''
    # list of student ids  
    students = df[df.staff == 0]
    student_ids = list(students.user_id.unique())

    student_accessed_outside_cohort = students[students.outside_cohort == 1]
    
    # Remove 'content/' from values in 'endpoint'
    student_accessed_outside_cohort['endpoint'] = student_accessed_outside_cohort['endpoint'].str.replace('content/', '')
    
    # Remove '/' and everything afterwards 
    student_accessed_outside_cohort['endpoint'] = student_accessed_outside_cohort['endpoint'].str.split('/').str[0]
    
    # replace nulls with 'home'
    student_accessed_outside_cohort['endpoint'] = student_accessed_outside_cohort['endpoint'].fillna('home')
    
    # program_id 1
    wd1_oc = student_accessed_outside_cohort[student_accessed_outside_cohort.program_id == 1]
    
    # program_id 2
    wd2_oc =student_accessed_outside_cohort[student_accessed_outside_cohort.program_id == 2]

    # program_id 3
    ds_oc = student_accessed_outside_cohort[student_accessed_outside_cohort.program_id == 3]
    
    return wd1_oc, wd2_oc, ds_oc
   

def webdev1_ml(wd1_oc):
    '''
    Analyze web development lessons and return the most common and least common lessons.

    Parameters:
        wd1_oc (pandas.DataFrame): The input DataFrame containing web development lesson data.

    Returns:
        tuple: A tuple containing two DataFrames:
            - The most common lessons DataFrame with columns 'Lesson' and 'Occurrences'.
            - The least common lessons DataFrame with columns 'Lesson' and 'Occurrences'.
    '''
    # removing blanks and getting top 5 
    wd1_oc = wd1_oc[wd1_oc.endpoint != '']

    # most common lesson
    wd1_mc_df = pd.DataFrame(wd1_oc.endpoint.value_counts().head()).reset_index()
    # removed not lessons
    wd1_oc = wd1_oc[~wd1_oc.endpoint.isin(['search', 'introduction-to-javascript.html'])]


    # create df of least common lessons
    
    wd1_ls_df = pd.DataFrame(wd1_oc.endpoint.value_counts()).reset_index()[:27].sort_values(by = "endpoint", ascending=True).head()

    return wd1_mc_df, wd1_ls_df
    
    

def webdev_viz(mc, lc):
    """
    Creates two separate subplots to visualize the most common and least common lessons
    that web development students accessed outside of their cohort.

    Args:
        mc (DataFrame): DataFrame containing data for the most common lessons. It should have
                        columns 'index' and 'endpoint' representing the lessons and their occurrences.
        lc (DataFrame): DataFrame containing data for the least common lessons. It should have
                        columns 'index' and 'endpoint' representing the lessons and their occurrences.

    Returns:
        None: This function displays the plots directly.

    """

    # Create two separate subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))


    # Plot for mc
    ax1.plot(mc['index'], mc['endpoint'])
    ax1.set_xlabel('Lessons')
    ax1.set_ylabel('Occurences')
    ax1.set_title('Most Common Lessons that Web Development Students Accessed Outside of their Cohort')


    # Plot for lc
    ax2.plot(lc['index'], lc['endpoint'])
    ax2.set_xlabel('Lessons')
    ax2.set_ylabel('Occurences')
    ax2.set_title('Least Common Lessons that Web Development Students Accessed Outside of their Cohort')



    # Adjust spacing between subplots
    plt.tight_layout()

    # Display the plots
    plt.show()


def webdev2_ml(wd2_oc):
    '''
    Analyze web development lessons and return the most common and least common lessons.

    Parameters:
        wd1_oc (pandas.DataFrame): The input DataFrame containing web development lesson data.

    Returns:
        tuple: A tuple containing two DataFrames:
            - The most common lessons DataFrame with columns 'Lesson' and 'Occurrences'.
            - The least common lessons DataFrame with columns 'Lesson' and 'Occurrences'.
    '''
    
    # most common
    # removing blanks and getting top 5 
    wd2_oc = wd2_oc[wd2_oc.endpoint != '']
    wd2_mc_df = pd.DataFrame(wd2_oc.endpoint.value_counts().head()).reset_index()
    # least common df
    wd2_oc = wd2_oc[~wd2_oc.endpoint.isin(['further-reading', 'login', 'setup', 'introduction', '2.00.02_Navigating_Excel'])]
    wd2_lc_df = pd.DataFrame(wd2_oc.endpoint.value_counts()).reset_index()[:49].sort_values(by = "endpoint", ascending=True).head()
    return wd2_mc_df, wd2_lc_df

def webdev2_viz(mc, lc):
    """
    Generate a visualization of the most common and least common lessons accessed by Web Development 2.0 students outside of their cohort.

    Parameters:
    - mc (DataFrame): A DataFrame containing the most common lessons accessed. It should have two columns: 'index' for lesson index and 'endpoint' for the number of occurrences.
    - lc (DataFrame): A DataFrame containing the least common lessons accessed. It should have two columns: 'index' for lesson index and 'endpoint' for the number of occurrences.

    Returns:
    None
    """
    # Create two separate subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))


    # Plot for mc
    ax1.plot(mc['index'], mc['endpoint'])
    ax1.set_xlabel('Lessons')
    ax1.set_ylabel('Occurences')
    ax1.set_title('Most Common Lessons that Web Development 2.0 Students Accessed Outside of their Cohort')


    # Plot for lc
    ax2.plot(lc['index'], lc['endpoint'])
    ax2.set_xlabel('Lessons')
    ax2.set_ylabel('Occurences')
    ax2.set_title('Least Common Lessons that Web Development 2.0 Students Accessed Outside of their Cohort')



    # Adjust spacing between subplots
    plt.tight_layout()

    # Display the plots
    plt.show()


def ds_ml(ds_oc):
    """
    Process a dataset of online courses.

    Args:
        ds_oc (pandas.DataFrame): The dataset of online courses.

    Returns:
        tuple: A tuple containing two pandas.DataFrame objects. The first dataframe (ds_mc_df) represents the most frequent lessons, 
               and the second dataframe (ds_lc_df) represents the least frequent lessons.
    """
    # removing blanks, search, and appendix and getting top 5 
    ds_oc = ds_oc[~ds_oc.endpoint.isin(['', 'appendix', 'search'])]
    # most lesson
    ds_mc_df = pd.DataFrame(ds_oc.endpoint.value_counts().head()).reset_index()
    # least lesson
    ds_lc_df = pd.DataFrame(ds_oc.endpoint.value_counts()).reset_index()[:26].sort_values(by = "endpoint", ascending=True).head()

    return ds_mc_df, ds_lc_df

def ds_viz(ds_mc, ds_lc):
    """Visualize most common and least common lessons accessed by Data Science students.

    Args:
        ds_mc (DataFrame): DataFrame containing data for most common lessons accessed.
        ds_lc (DataFrame): DataFrame containing data for least common lessons accessed.

    Returns:
        None

    Plots two subplots showing the most common and least common lessons accessed by Data Science students.
    Each subplot displays the occurrences of lessons on the y-axis and the lesson index on the x-axis.
    The first subplot represents the most common lessons accessed, and the second subplot represents the least common lessons accessed.
    The subplots are displayed in a single figure with a size of 8x6.

    The x-axis label for both subplots is set to 'Lessons'.
    The y-axis label for both subplots is set to 'Occurrences'.
    The title for the first subplot is set to 'Most Common Lessons that Data Science Students Accessed Outside of their Cohort',
    and the title for the second subplot is set to 'Least Common Lessons that Data Science Students Accessed Outside of their Cohort'.

    The function adjusts the spacing between the subplots using plt.tight_layout() to avoid overlapping.
    Finally, the plots are displayed using plt.show().
    """

    # Create two separate subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))


    # Plot for ds_mc
    ax1.plot(ds_mc['index'], ds_mc['endpoint'])
    ax1.set_xlabel('Lessons')
    ax1.set_ylabel('Occurences')
    ax1.set_title('Most Common Lessons that Data Science Students Accessed Outside of their Cohort')


    # Plot for ds_lc
    ax2.plot(ds_lc['index'], ds_lc['endpoint'])
    ax2.set_xlabel('Lessons')
    ax2.set_ylabel('Occurences')
    ax2.set_title('Least Common Lessons that Data Science Students Accessed Outside of their Cohort')



    # Adjust spacing between subplots
    plt.tight_layout()

    # Display the plots
    plt.show()
