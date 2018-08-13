# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:53:19 2018

@author: YudakovSA
"""
report_indices_sql = (''' 
    select ti.identificator, \
    reptype.mnemo, \
    typeind.link_index \
    from t_rmm_report_types_indexes typeind, t_index ti, t_report_type reptype \
    where typeind.link_index = ti.id \
    and typeind.link_report_type = reptype.id \
    and reptype.link_report_type_class = 2 \
    order by 1 \
    ''') 
 
