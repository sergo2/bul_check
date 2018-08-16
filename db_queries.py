# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:53:19 2018

@author: YudakovSA
"""
report_indices_sql = (''' 
    select \
        '' as change, \
        '' as date_of_index, \
        tc.name_en, \
        coalesce(tc.code_sp, tc.code) as index_code, \
        tc.key as index_key, \
        '' as gics_code, \
        cur.mnemo as iso_code, \
        val.close_val as index_value, \
        val.volume_money as close_market_cap, \
        tc.divisor as close_divisor, \
        val.count_ as close_count, \
        val.return_close as daily_return, \
        val.dividend as index_dividend, \
        val.mc_index as adj_market_cap, \
        tc_adj.divisor as adj_divisor, \
        val.mc_index_tom as adj_count, \
        reptype.mnemo as rep_type, \
        tc.id as composition_id_cls, \
        tc_adj.id as composition_id_adj \
    from  t_index ti, t_composition tc, t_composition tc_adj, \
            t_rmm_report_types_indexes typeind, t_report_type reptype, \
            t_currency cur, t_index_daily_values val \
    where ti.id = tc.link_index \
    and ti.id = tc_adj.link_index \
    and typeind.link_index = ti.id \
    and typeind.link_report_type = reptype.id \
    and tc.link_currency = cur.id \
    and tc.id = val.link_composition \
    and reptype.link_report_type_class = 2 \
    and val.date_ = ? \
    and tc.id =                    \
        (select current_version_id from get_versions_by_date(ti.id, ?) \
        ) \
    and tc_adj.id =                \
        (select next_version_id from get_versions_by_date(ti.id, ?) \
        ) \
    order by index_code \
    ''')
        
get_next_calc_date_sql = ('''        
    create or alter procedure get_next_calc_date (input_date date, calendar_type integer) \
                    returns (next_date date) \
    as \
    begin \
        for select min(calendar.date_) \
            from t_calendar_date calendar \
            where calendar.link_calendar_type = :calendar_type \
            and f_working_day = 1 \
            and date_ > :input_date \
            into :next_date \
        do \
        begin \
          suspend; \
        end \
    end; \
    ''')

get_versions_by_date_sql = ('''  
    create or alter procedure get_versions_by_date (index_id integer, input_date date) \
                    returns (current_version_id integer, next_version_id integer) \
    as \
    declare \
        next_date date; \
    begin \
        select max(id) \
        from t_composition tc1 \
        where link_composition_state in (2,4,5) \
        and :input_date between activation_date and coalesce(deactivation_date, '2050-01-01') \
        and tc1.link_index = :index_id \
        into :current_version_id; \
     \
        select next_date \
        from get_next_calc_date(:input_date, 1) \
        into :next_date; \
     \
        select max(id) \
        from t_composition tc1 \
        where link_composition_state in (2,4,5) \
        and :next_date between activation_date and coalesce(deactivation_date, '2050-01-01') \
        and tc1.link_index = :index_id \
        into :next_version_id; \
     \
        suspend; \
     \
    end; \
    ''') 
