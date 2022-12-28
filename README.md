# Machine Learning Practice

Data playground for improving machine learning skills using Kaggle datasets.

To create the <code>mlp</code> environment run:

<code>conda env create -f environment.yml</code>

## Contents
### 1. INGV - Volcanic Eruption Prediction
<a href="https://www.kaggle.com/competitions/predict-volcanic-eruptions-ingv-oe/">Link to Kaggle Competition</a>

Data size is 31.25 GB and contains 8953 files.

Please download the data zip file directly from Kaggle by running the following code within the <code>data/</code> directory:

<code>kaggle competitions download -c predict-volcanic-eruptions-ingv-oe</code> 

The data zip file can then be unzipped via:

<code>unzip predict-volcanic-eruptions-ingv-oe.zip</code>

For the data zip file to download successfully, please ensure your <code>~/.kaggle</code> folder contains a valid Kaggle API token <code>kaggle.json</code>.

If not, please create a new token from within your Kaggle account settings, then move the token from the <code>Downloads</code> folder to the <code>~/.kaggle</code> folder.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gems-hcl4517/Machine_Learning_Practice/blob/main/INGV_Volcanic_Eruption_Prediction/model.ipynb)<br>

### 2. Titanic - Machine Learning from Disaster
<a href="https://www.kaggle.com/competitions/titanic">Link to Kaggle Competition</a>
