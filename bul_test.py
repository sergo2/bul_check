import pytest
import pandas as pd

bul_file_1 = "C:\\Python_progs\\bul_tests\\bul1.sdl"
bul_file_2 = ""

bul_df_1 = pd.read_csv(bul_file_1, sep='\t')
print(bul_df_1.shape)

