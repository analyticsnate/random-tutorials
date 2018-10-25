def add_to_column_names(df, text, exclude=None):
    """
    Adds a string to all column names of dataframe
    
    Params:
    -------
    df : dataframe
    the dataframe with the column names to modify
    
    text : string
    the text to add to the column names
    
    exclude : list of column name strings
    use this list to skip adding the text to the column name
    """
    # create dict to store old : column names
    rename_dict = {}

    # get a string list of column names from the dataframe
    col_list = df.columns.tolist()

    # iterate through the string list of column names
    # add the word to the string and store in the dict
    for col in col_list:
        if col not in exclude:
            rename_dict[col] = text + col

    # use rename_dict in the pandas rename() method
    # that applies the name change to the data frame
    df.rename(rename_dict, inplace=True)

    return df
