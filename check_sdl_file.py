# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:35:36 2018

@author: YudakovSA
"""
def check_sdl_file(sdl_file_name, df_index):
    df_sdl = pd.read_csv(sdl_file_name, sep='\t', engine='python', skipfooter = 1)
    # Replace blank spaces
    df_sdl.columns = df_sdl.columns.str.strip().str.upper().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    
    # Filtering in only SDL table rows
    df_index = df_index[(df_index['REP_TYPE']=="RT_MOEX_SDL") & (df_index['FILE_EXISTS']=="exists")]

    # Comparing
    for i, table_rows in df_index.iterrows():
        print(table_rows)
    
    
