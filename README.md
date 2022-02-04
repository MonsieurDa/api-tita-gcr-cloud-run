# General
An simple example on how to deploy machine learning model api on GCR

# To use this repo we have to :
* create a gcp project and enable billing
* Activate containerregistry and artifactregistry api's
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



