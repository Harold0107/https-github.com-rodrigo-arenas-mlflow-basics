#!/bin/bash

mlflow server --backend-store-uri mlflow_db \
              --default-artifact-root ./mlflowruns \
              --host 0.0.0.0 \
              --port 5000