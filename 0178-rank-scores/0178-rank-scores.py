import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    scores1=scores.drop("id",axis=1).sort_values(by="rank",ascending=True)
    return scores1
    