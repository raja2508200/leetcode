import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    filter1=(world["area"]>=3000000)|(world["population"]>=25000000)
    final=world[filter1][["name","area","population"]]
    return final
    