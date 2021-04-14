import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
import numpy as np
from itertools import product, chain, combinations


def calc_possible_combinations(ser):
    k = ser.name[0]
    n = ser.name[1]
    res = []
    res.extend([l for l in combinations(range(1, 10), k) if sum(l) == n])
    return res


idx = pd.MultiIndex.from_tuples(list(
    chain(*[list(product([k], list(range(sum(range(1, k + 1)), 1 + sum(range(10 - k, 10)))))) for k in range(2, 9)])),
                                names=['k', 'n'])
df = pd.DataFrame(np.zeros(len(idx)), index=idx)
df = df.apply(calc_possible_combinations, axis=1)
df = df.unstack().fillna('N/A')

n = st.slider("Sum (n)", 3, 44, value=3)
k = st.slider("Window size (k)", 2, 8, value=2)

if df.loc[k, n] == 'N/A':
    st.write(f'Impossible combination of k={k} and n={n}')
else:
    cols = [f'n_{v}' for v in range(1, k+1)]
    idx = [f'sol_{v}' for v in range(1, len(df.loc[k, n]) + 1)]
    sol_df = pd.DataFrame(data=df.loc[k, n], index=idx, columns=cols)
    st.dataframe(sol_df)

HtmlFile = open("/app/portfolio/streamlit/ad.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
components.html(source_code)