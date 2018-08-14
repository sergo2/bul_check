import pandas as pd
from source_config import * 

bul_file_sdl = path_to_report_files + "#20180810#_MOEX.SDL"

df_sdl = pd.read_csv(bul_file_sdl, sep='\t', engine='python', skipfooter = 1)
# Replace blank spaces
df_sdl.columns = df_sdl.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

for i in df_sdl.columns:
    print(i)