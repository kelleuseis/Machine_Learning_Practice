# Machine Learning Practice

Data playground for improving machine learning skills using Kaggle datasets.

To create the <code>mlp</code> environment run:

```bash
conda env create -f environment.yml
```

## Contents
### INGV - Volcanic Eruption Prediction :volcano:
<a href="https://www.kaggle.com/competitions/predict-volcanic-eruptions-ingv-oe/">Link to Kaggle Competition</a>

> What if scientists could anticipate volcanic eruptions as they predict the weather? While determining rain or shine days in advance is more difficult, weather reports become more accurate on shorter time scales. A similar approach with volcanoes could make a big impact. Just one unforeseen eruption can result in tens of thousands of lives lost. If scientists could reliably predict when a volcano will next erupt, evacuations could be more timely and the damage mitigated.

> Enter Italy's Istituto Nazionale di Geofisica e Vulcanologia (INGV), with its focus on geophysics and volcanology. The INGV's main objective is to contribute to the understanding of the Earth's system while mitigating the associated risks. Tasked with the 24-hour monitoring of seismicity and active volcano activity across the country, the INGV seeks to find the earliest detectable precursors that provide information about the timing of future volcanic eruptions.

Data size is 31.25 GB and contains 8953 files.

Download the data zip file directly from Kaggle by running the following code within the <code>data/</code> directory:

```bash
kaggle competitions download -c predict-volcanic-eruptions-ingv-oe
```

The data zip file can then be unzipped via:

```bash
unzip predict-volcanic-eruptions-ingv-oe.zip
```

For the data zip file to download successfully, please ensure your <code>~/.kaggle</code> folder contains a valid Kaggle API token <code>kaggle.json</code>.

If not, please create a new token from within your Kaggle account settings, then move the token from the <code>Downloads</code> folder to the <code>~/.kaggle</code> folder.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gems-hcl4517/Machine_Learning_Practice/blob/main/INGV_Volcanic_Eruption_Prediction/model.ipynb)<br>

<p align="center">~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</p>

### Warm-up Exercises :fire:
-----------------------------------------------------------------------------------------------------
Each exercise includes the following:

<code>data/</code>: contains the dataset description, train and test sets, and sample prediction CSV file

<code>real_data/</code>: contains the full dataset, and/or kaggle leaderboard score distribution

<code>model.ipynb</code>: sample ML workflow using Jupyter Notebook

> This is a fun competition aimed at helping you get started with machine learning.  While the dataset is publicly available on the internet, looking up the answers defeats the entire purpose. So seriously, don't do that.

-----------------------------------------------------------------------------------------------------
### 1. Titanic - Machine Learning from Disaster :ship:

<p align="center">
	<img src="https://github.com/gems-hcl4517/Machine_Learning_Practice/blob/main/Titanic_Machine_Learning_from_Disaster/images/titanic_info.GIF?raw=true" /><br>
	<sub><sup>Adapted from GIF animation by Artistosteles, Wikimedia Commons</sup></sub>
</p>

<a href="https://www.kaggle.com/competitions/titanic">Link to Kaggle Competition</a>

### 2. House Prices - Advanced Regression Techniques :house:
<a href="https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques">Link to Kaggle Competition</a>

### 3. Digit Recognizer :1234:
<a href="https://www.kaggle.com/competitions/digit-recognizer/overview">Link to Kaggle Competition</a> 

<p align="center">~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</p>

### Check your score! :chart_with_upwards_trend:
<code>score.py</code> is a python script for evaluating final model performance on the test set, callable within each exercise directory via:<br>
```bash
python ../score.py -f [prediction csv filepath]
```
