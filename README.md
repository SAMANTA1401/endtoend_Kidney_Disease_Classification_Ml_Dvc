# Kidney_Disease_Classification_Ml_Dvc

##workflows

1. update config.yaml
2. update secrets.yaml[optional]
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the dvc.yaml
10. app.py


###step1:

clone repository

```bash
https://github.com/SAMANTA1401/Kidney_Disease_Classification_Ml_Dvc.git
```
###step2:

create a conda enviroment after opening the repository

```bash
conda create -n kidney python=3.11 -y
```

```bash
conda activate kidney
```
###step3:
```bash
pip install -r requirements.txt
```

## Mlflow

[Documentation](https://mlflow.org/docs/latest/index.html)

#### cmd
-mlflow ui

###dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/SAMANTA1401/Kidney_Disease_Classification_Ml_Dvc.mlflow \
MLFLOW_TRACKING_USERNAME=SAMANTA1401 \
MLFLOW_TRACKING_PASSWORD=922b4b5be2933b85c40e93033b823635135b6510 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/SAMANTA1401/Kidney_Disease_Classification_Ml_Dvc.mlflow 
export MLFLOW_TRACKING_USERNAME=SAMANTA1401 
export MLFLOW_TRACKING_PASSWORD=922b4b5be2933b85c40e93033b823635135b6510 
```
##### use 'set'  instead of 'export' if you are using windows or anaconda prompt use this comand every time after restarting cmd and vscode then 

###dvc cmd
```bash
dvc iniit
dvc repro
dvc dag
```
### This model is not working good as very less number of images are used and  epochs is 1 and trained for only one times no evaluation is done .
