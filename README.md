## Assets in repo

* `requirements.txt`:  [View requirements.txt](https://github.com/alonmar/usuarios-y-cesiones/blob/main/requirements.txt)
* `cli.py`: [View cli.py](https://github.com/alonmar/usuarios-y-cesiones/blob/main/cli.py)
* `app.py`:  [View app.py](https://github.com/alonmar/usuarios-y-cesiones/blob/main/app.py)
* `mlib.py`:  [View mlib.py](https://github.com/alonmar/usuarios-y-cesiones/blob/main/mlib.py) Model Handling Library
* `Datos prueba.xlsx`: [View data](https://github.com/alonmar/usuarios-y-cesiones/tree/main/data/01_raw) Data
* `kmeans_model.joblib`: [View kmeans_model.joblib](https://github.com/alonmar/usuarios-y-cesiones/blob/main/kmeans_model.joblib)
*  `eda.ipynb`:  [eda.ipynb](https://github.com/alonmar/usuarios-y-cesiones/blob/main/eda.ipynb)


### CLI Tools

There are two cli tools.  First, the main `cli.py` is the endpoint that serves out predictions.
To predict the cluster of an user you use the following: 

`$ python .\cli.py --monactivo 0 --meansales 0 --meancesiones 0 --proyecsales 0 --proyecbuys 0`


### Flask Microservice

The Flask ML Microservice can be run many ways.

#### Containerized Flask Microservice Locally

You can run the Flask Microservice as follows with the commmand: `python app.py`.

```
$ python app.py 
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 128-376-958
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
```

after run flask to serve a prediction against the application, run the `predict.sh`.

```
$ ./predict.sh                             
Port: 8080
{
  "Cluster": 0
}

```


