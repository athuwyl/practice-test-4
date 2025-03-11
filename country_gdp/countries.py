import pandas

df = pandas.read_csv("country_gdp.csv")
df['population'] = df['population'].apply(lambda x: int(x.replace(",", "")))

def developed_countries(df: pd.DataFrame) -> pd.DataFrame:
  developed = df[(df['gdp_per_cap'] > '12000') & (df['unemployment_rate'] <= '7.5%')]
  return developed

  df.drop(number, gov_type)
  
  total_gdp = df[(df['gdp_per_cap']) * df[('population')]]
  
  

