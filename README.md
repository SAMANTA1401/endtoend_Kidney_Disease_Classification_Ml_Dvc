# Kidney_Disease_Classification_Ml_Dvc

### Classification of Normal and Tumour kidney from ct scan images with vgg16 model



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



###dvc cmd
```bash
dvc iniit
dvc repro
dvc dag
```
#### This model is not working good as very less number of images are used and  epochs is 1 and trained for only one times no evaluation is done .

## AWS-CICD-Deployment-with-Github-Actions

### 1.Login to AWS console.

### 2.Create IAM user for deployment

####with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


####Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

####Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

### 3.  Create ECR repo to store/save docker image
- Save the URI:987001014426.dkr.ecr.eu-north-1.amazonaws.com/kidney

### 4.Create EC2 machine (Ubuntu)
### 5.Open EC2 and Install docker in EC2 Machine:

```bash
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```
### 6.Configure EC2 as self-hosted runner:

setting>actions>runner>new self hosted runner> choose os> then run command one by one

### 7. Setup github secrets:

```bash
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = kidney
```