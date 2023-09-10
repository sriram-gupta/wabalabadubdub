import pickle
model = pickle.load(open('./train/height_prediction_model','rb'))

def HeightPredictor(weight):
    pred =  model.predict([[weight]])
    return pred[0][0]

