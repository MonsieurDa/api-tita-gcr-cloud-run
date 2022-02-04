"""
This file defines the server
and the class we use to predict using our trained classifier
We will put the two into one file to save some time for the exercice.
In practice make sure to have them in separate classes.
"""
from concurrent.futures import thread
from multiprocessing.managers import ValueProxy
import os
import uvicorn
import numpy as np
from fastapi import FastAPI, HTTPException
from joblib import load
from pydantic import BaseModel
from sklearn.tree import DecisionTreeClassifier



# Define object we classify : cette classe est utiliser un modele de base pour faire nos prédiction
class PersonInformation(BaseModel):
    sex: str
    pclass: int

class PredictionOut(BaseModel):
    value = float

# on peut aussi définir un modèle de base pour la sortie


# une class pour la prédiction 
class SurvivePredictor:
    """
    Holds the actual process of doing the prediction
    """

    def __init__(self):
        self.clf: DecisionTreeClassifier = load("./model_weights/clf.bin")

    def predict(self, item: PersonInformation):
        # make sure that here the order is the same as in the model training
        print("item:", item)
        x = np.array([1 if item.sex == "female" else 0, item.pclass])
        x = x.reshape(1, -1)
        # be careful to only transform and not fit
        print("numeric representation:", x)
        PredictionOut.value = self.clf.predict_proba(x)
        y = PredictionOut.value
        print("survival probability:", y)
        # y looks now like: [[0.78 0.21]] so the second number is probability of survived
        return y[0][1]





#####################################
##################################### server
#####################################

# initialiser l'api
app = FastAPI()
predictor = SurvivePredictor()


# Server Definition
@app.get("/")
def root(): # = main entrypoint
    #return {"GoTo": "/docs"}

    return {"check the link" : "/docs"}


@app.post("/will_survive")
def is_user_item(request: PersonInformation):
    try:
        return {"survival_probability": predictor.predict(request)}
    except:
        raise HTTPException(status_code=418, detail="Exceptions can't be handheld by a teapot")


#PORT = int(os.environ.get("PORT",8080))
#if __name__ =="__main__":
#    uvicorn.run("main:app", host='0.0.0.0', port=PORT)