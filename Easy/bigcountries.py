import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Select only countries with area >= 3M or population >= 25M
    return world.loc[
        (world.area >= 3000000) | (world.population >= 25000000),
        ["name", "population", "area"],
    ]
