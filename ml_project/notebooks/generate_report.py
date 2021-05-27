import pandas as pd
from pandas_profiling import ProfileReport

DATA_PATH = 'data/raw/heart.csv'
RESULT_PATH = 'notebooks/report.html'

df = pd.read_csv(DATA_PATH)

profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file(RESULT_PATH)
