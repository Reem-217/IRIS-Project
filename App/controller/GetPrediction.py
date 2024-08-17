def GetPrediction(model, Inputs:list):
    res= {
        0: "Iris-setosa",
        1: "Iris-versicolor",
        2: "Iris-virginica"
    }
    
    predictions= model.predict([Inputs])[0]
    return res[predictions]