import os
import pandas as pd


def read_excel(excel_file, sheet_name, excel_dir='excel', engine='openpyxl'):
    return pd.read_excel(
        os.path.join(os.path.dirname(__file__), excel_dir, excel_file),
        sheet_name=sheet_name,
        engine=engine,
    )


def filter_deg(df):
    return (df.assign(LFC=lambda x: round(x['Log2 fold change'], 2),
                      pval=lambda x: x['Adjusted p-value'].apply(lambda x: '%.1E' % x))
            .filter(['Gene ID', 'LFC', 'pval', 'Gene symbol', 'Gene name'])
            .rename(columns={'pval':'Adj p-val'}))


def filter_dmc(df):
    return (df.assign(qval=lambda x: x['Q-value'].apply(lambda x: '%.1E' % x))
            .sort_values(by='Q-value', ignore_index=True)
            .filter(['Chromosome', 'Start', 'Region', 'Mdiff', 'qval',
                     'Gene ID', 'Gene symbol', 'Gene name'])
            .rename(columns={'qval':'Q-value', 'Start':'Pos'}))


def filter_dmg(df):
    return (df.filter(['Gene ID', 'Total', 'GB', 'Exon', 'Intron',
                       'P', 'P250', 'P1K', 'P5K', 'Flanks',
                       'Gene symbol', 'Gene name'])
            .sort_values(by=['Total', 'GB', 'P', 'Exon', 'Intron', 'P250', 'P1K', 'P5K', 'Flanks'],
                         ascending=False, ignore_index=True))


def write_csv(pd, ofile_name, data_dir='_data'):
    pd.to_csv(
        os.path.join(os.path.dirname(__file__), "..", data_dir, ofile_name),
        index=False
    )


def generate_csv(excel_file, sheet_name, filter_func, ofile_name):
    (read_excel(excel_file, sheet_name)
     .pipe(filter_func)
     .pipe(write_csv, ofile_name=ofile_name))


# DEG L2:L1
excel_file = 'Dataset_01_DEG_L2L1.xlsx'
sheet_name = 'Gonad (DEGs)'
ofile_name = 'degl2l1.csv'
generate_csv(excel_file, sheet_name, filter_deg, ofile_name)

# DEG L2:L1
excel_file = 'Dataset_02_DEG_L3L1.xlsx'
sheet_name = 'Gonad (DEGs)'
ofile_name = 'degl3l1.csv'
generate_csv(excel_file, sheet_name, filter_deg, ofile_name)

# DMC L2:L1
excel_file = 'Dataset_03_DMC_L2L1.xlsx'
sheet_name = 'Gonad (DMCs)'
ofile_name = 'dmcl2l1.csv'
generate_csv(excel_file, sheet_name, filter_dmc, ofile_name)

# DMC L3:L1
excel_file = 'Dataset_04_DMC_L3L1.xlsx'
sheet_name = 'Gonad (DMCs)'
ofile_name = 'dmcl3l1.csv'
generate_csv(excel_file, sheet_name, filter_dmc, ofile_name)

# DMG L2:L1
excel_file = 'Dataset_07_DMG_L2L1.xlsx'
sheet_name = 'Gonad'
ofile_name = 'dmgl2l1.csv'
generate_csv(excel_file, sheet_name, filter_dmg, ofile_name)

# DMG L3:L1
excel_file = 'Dataset_08_DMG_L3L1.xlsx'
sheet_name = 'Gonad'
ofile_name = 'dmgl3l1.csv'
generate_csv(excel_file, sheet_name, filter_dmg, ofile_name)

