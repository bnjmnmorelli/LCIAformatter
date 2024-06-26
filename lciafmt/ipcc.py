# ipcc.py (lciafmt)
# !/usr/bin/env python3
# coding=utf-8
"""
This module contains functions needed to compile LCIA methods from IPCC
"""

import pandas as pd
from lciafmt.util import log, datapath
from lciafmt.df import lciafmt_cols

### IPCC data for each AR were sourced from the following:
## AR4: Table 2.14 (https://archive.ipcc.ch/publications_and_data/ar4/wg1/en/errataserrata-errata.html#table214)
## AR5: Table 8.A.1 (https://archive.ipcc.ch/pdf/assessment-report/ar5/wg1/WG1AR5_Chapter08_FINAL.pdf)
## AR6: Table 7.SM.7 (https://github.com/IPCC-WG1/Chapter-7/blob/main/data_output/7sm/metrics_supplement_cleaned.csv)

def get() -> pd.DataFrame:
    """Generate a method for IPCC in standard format.
    :return: DataFrame of method in standard format
    """
    log.info("get method IPCC")

    filename = 'IPCC_GWP_values.csv'
    df = pd.read_csv(datapath / filename)
    df['Indicator'] = df['AR'] + '-' + df['Parameter'].str.replace('GWP', '')
    df['Method'] = 'IPCC'
    df['Indicator unit'] = 'kg CO2 eq'
    df['Context'] = 'air'
    df['Unit'] = 'kg'
    df = df[df['Value'] != '(no data)']
    df = df.dropna(subset=['Name'])
    df['Value'] = df['Value'].astype('float')
    df = df.rename(columns={'Name': 'Flowable',
                            'CAS': 'CAS No',
                            'Value': 'Characterization Factor'})
    df = df.reindex(columns=lciafmt_cols)
    df = df.fillna('')

    return df


if __name__ == "__main__":
    import lciafmt
    method = lciafmt.Method.IPCC
    df = lciafmt.get_method(method)
    mapped_df = lciafmt.map_flows(df, system=method.get_metadata().get('mapping'))
    mapped_df2 = lciafmt.util.collapse_indicators(mapped_df)
