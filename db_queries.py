# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:53:19 2018

@author: YudakovSA
"""
report_indices_sql = (''' 
    select  coalesce(tc.code_sp, tc.code) as code_sp, \
            reptype.mnemo, \
            typeind.link_index \
    from  t_index ti, t_composition tc, \
            t_rmm_report_types_indexes typeind, t_report_type reptype \
    where tc.link_index = ti.id \
    and typeind.link_index = ti.id \
    and typeind.link_report_type = reptype.id \
    and tc.link_composition_state = 4 \
    and reptype.link_report_type_class = 2   -- S&P \
    order by tc.code \
    ''') 
 
