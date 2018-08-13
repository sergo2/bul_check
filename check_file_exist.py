# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:58:26 2018

@author: YudakovSA
"""
import fdb
import pandas as pd
import os

from source_config import *
from db_queries import *

def report_file_name(date, index_code, report_index_type):
    report_file_name = "#" + date + "#_"
    
    if report_index_type == "RT_MOEX_SDL":
        report_file_name += "MOEX"
    else:
        report_file_name += index_code
        
    report_file_name_suffix = ""
    
    if report_index_type == "RT_MOEX_SDL":
        report_file_name_suffix = ".SDL"
    elif report_index_type == "RT_CLS_SDC":
        report_file_name_suffix = "_CLS.SDC"
    elif report_index_type == "RT_ADJ_SDC":
        report_file_name_suffix = "_ADJ.SDC"
    elif report_index_type == "RT_SDE":
        report_file_name_suffix = ".SDE"
    
    report_file_name += report_file_name_suffix
    return report_file_name

def report_file_exists(file_name):
    full_file_name = path_to_report_files + file_name
    if os.path.isfile(full_file_name):
        if os.path.getsize(full_file_name) > 0:
            result = "Exists"
        else:
            result = "Exists but empty"
    else:
        result = "Doesn't exist"
    return result

try:
    print("Checking against " + db_config['database'] + " database at " + db_config['host'])
    con1 = fdb.connect(host=db_config['host'], database=db_config['database'], \
                   user=db_config['user'], password=db_config['password'], charset='UTF8')

    df_index = pd.read_sql(report_indices_sql, con1)
    df_index = df_index.sort_values(by=['CODE_SP', 'MNEMO']) # sort by index code
    df_index['FILE_NAME'] = ""
    df_index['FILE_EXISTS'] = ""

    for index, row in df_index.iterrows():
        report_index_file = row['CODE_SP'].strip()
        report_index_type = row['MNEMO'].strip()
        rep_file_name = report_file_name(date_to_check, report_index_file, report_index_type)
        df_index.loc[index, 'FILE_NAME'] = rep_file_name
        df_index.loc[index, 'FILE_EXISTS'] = report_file_exists(rep_file_name)
        # can't source assigned values because iterrows operates on a copy of DF
        print(row['CODE_SP'] + " " + row['MNEMO'] + " " + rep_file_name + " " + report_file_exists(rep_file_name))
        
except Exception as error:
    print("Can't open " + db_config['database'] + " database at " + db_config['host'])
    print('Error message: {}'.format(error))
    
con1.close()