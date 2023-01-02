import os
import argparse

import pandas as pd
import scipy.interpolate as si
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

real_path = os.sep.join((os.getcwd(),
                         'real_data', 'kaggle_predictions.csv'))
assert os.path.exists(real_path), "File not found: real_data/kaggle_predictions.csv"
real = pd.read_csv(real_path)


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type = str, help = 'Path to Prediction CSV File')
args = parser.parse_args()


if args.file is None:
    args.file = "data/predictions.csv"

pred_path = os.sep.join((os.getcwd(), args.file))
assert os.path.exists(pred_path), f"File not found: {args.file}"
pred = pd.read_csv(pred_path)


rank_path = os.sep.join((os.getcwd(),
                         'real_data', 'leaderboard_score.csv'))
assert os.path.exists(rank_path), "File not found: real_data/leaderboard_score.csv"
rank = pd.read_csv(rank_path)


pwcubic = si.interp1d(rank.Percentile, rank.Score,
                      'cubic', fill_value="extrapolate")
pct = np.linspace(0,100,10000)
df = pd.DataFrame({'pct':pct,'score':pwcubic(pct)})


_,dirname = os.path.split(os.getcwd())


if __name__ == "__main__":
    
    colname = {"Digit_Recognizer":"Label", "Titanic_Machine_Learning_from_Disaster":"Survived",\
               "House_Prices_Advanced_Regression_Techniques":"SalePrice"}
    
    assert len(pred.index)==len(real.index), \
            f"CSV file should contain {len(real.index)} predictions, got {len(pred.index)} instead"
    assert colname[dirname] in pred.columns, \
            f'Prediction column needs to be labelled as {colname[dirname]}'

    acc_score = accuracy_score(pred[colname[dirname]], real[colname[dirname]])

    print(f'Accuracy Score: {np.round(acc_score, 6)}')
    print(f'Indicative Percentile Rank: {np.round(*df[df.score>=acc_score].head(1).pct.values, 6)}')
