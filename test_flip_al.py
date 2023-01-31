import pandas as pd
import numpy as np

zscores = np.array([1, -1, 2, 3])

gwas_a1 = pd.Series(['G', 'C', 'A', 'T'])
gwas_a2 = pd.Series(['C', 'GGG', 'T', 'A'])

gwas = gwas_a1 + gwas_a2

ref_a1 = pd.Series(['G', 'C', 'A', 'A'])
ref_a2 = pd.Series(['C', 'GG', 'T', 'T'])

ref = ref_a1 + ref_a2
ref_rev = ref_a2 + ref_a1

match_flags = gwas == ref
flip_flags = gwas == ref_rev

