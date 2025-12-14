import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views.query("author_id==viewer_id")
    df = df.rename(columns={"author_id": "id"})
    df = df[["id"]].drop_duplicates()
    return df.sort_values("id")
