import mlflow
import pandas as pd
logged_model = 'models:/Wine_Elasticnet_Sklearn_Regressor/Production'

data = pd.read_csv('winequality-red.csv')

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)


print(loaded_model.predict(data))
