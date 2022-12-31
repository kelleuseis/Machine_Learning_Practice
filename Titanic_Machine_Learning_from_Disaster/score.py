import os
import argparse

import pandas as pd
import scipy.interpolate as si
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

real_path = os.sep.join((os.path.dirname(__file__), 
                         'real_data', 'kaggle_predictions.csv'))
real = pd.read_csv(real_path)

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type = str, help = 'Path to Prediction CSV File')
args = parser.parse_args()

if args.file is None:
    args.file = "data/predictions.csv"

assert os.path.exists(args.file), "File not found"
pred_path = os.sep.join((os.path.dirname(__file__), args.file))
pred = pd.read_csv(pred_path)


rank_path = os.sep.join((os.path.dirname(__file__), 
                         'real_data', 'leaderboard_score.csv'))
rank = pd.read_csv(rank_path)

pwcubic = si.interp1d(rank.Percentile, rank.Score, 
                      'cubic', fill_value="extrapolate")
pct = np.linspace(0,100,10000)
df = pd.DataFrame({'pct':pct,'score':pwcubic(pct)})


if __name__ == "__main__":
    assert len(pred.index)==418, f"CSV file should contain 418 predictions, got {len(pred.index)} instead"
    assert 'Survived' in pred.columns, 'Prediction column needs to be labelled as "Survived"'
    
    acc_score = accuracy_score(pred.Survived, real.Survived)
    print(f'Accuracy Score: {np.round(acc_score, 6)}')
    print(f'Indicative Percentile Rank: {np.round(*df[df.score>=acc_score].head(1).pct.values, 6)}')


