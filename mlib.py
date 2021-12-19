import pandas as pd

import joblib

def load_model(model="kmeans_model.joblib"):
    """Grabs model from disk"""

    clf = joblib.load(model)
    return clf


def data():
    """Read data"""
    df = pd.read_excel('data/01_raw/Datos prueba.xlsx', index_col=0)
    return df

def cluster_0(data_to_predict):
    ''' adsad '''
    # unit test
    sum_values = sum(data_to_predict.values())

    return sum_values 
    
def cluster_1(data_to_predict):

    sum_values = data_to_predict['Monto activo'] + data_to_predict['proyeccion ventas'] + data_to_predict['proyeccion compras']

    return sum_values

def predict(data_to_predict):
    """Takes weight and predicts height"""

    clf = load_model()  # loadmodel

    if cluster_0(data_to_predict) == 0:
        cluster = 0
    elif cluster_1(data_to_predict) == 0:
        cluster = 1
    else:
        data_to_predict = pd.DataFrame([data_to_predict])
        cluster = clf.predict(data_to_predict)[0]+2

    return cluster
