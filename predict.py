import mlflow
import pandas as pd
logged_model = 'wasbs://<MY-STORAGE-URI>/runs/<EXPERIMENT_ID>/<RUN_ID>/artifacts/model'

data = pd.read_csv('winequality-red.csv')

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)


print(loaded_model.predict(data))
