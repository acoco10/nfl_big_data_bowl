
import pandas as pd 
import matplotlib.pyplot as plt



def is_alpha(player):
    return "".join([letter.lower() for letter in player if letter.isalpha()])
    
def clean_qb_tables(df):
    df.columns = [col.lower() for col in df.columns]
    df["player"] = df.player.apply(is_alpha)
    df = df[df.pos == "QB" ]
    df = df["player"]
    return df