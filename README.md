# General
[![api-tita-gcr-cloud-run](https://github.com/MonsieurDa/api-tita-gcr-cloud-run/actions/workflows/cloudrun.yml/badge.svg?branch=master)](https://github.com/MonsieurDa/api-tita-gcr-cloud-run/actions/workflows/cloudrun.yml)

An simple example on how to deploy machine learning model api on GCR

# To use this repo we have to :
* create a gcp project and enable billing
* Activate containerregistry api and cloud run
* create a service account (SA) with necessary IAM roles
* download json of the SA
* setup github secrets informations 


# CI/CD with GitHub actions 
steps : 
* 1 - set up python
* 2 - Install dependencies with requirements.txt
* 3 - Lint with fake8
* 4 - Unittest python script
* 5 - and Build and Push docker Image on gcr

###  PS : Once the API deployed on cloud run, you have to allow unauthenticated invocations, add "allUsers" as a principal and assign it the "Cloud Run invoker" role to allow public url access. This can be done in https://console.cloud.google.com/run on permissions window.



