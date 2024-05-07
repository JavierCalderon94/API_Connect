# API_Connect
Este proyecto consiste en el desarrollo de una API utilizando FASTAPI para analizar datos de inversión en publicidad y realizar predicciones de ventas. Se ha creado una base de datos SQLite que contiene datos de inversión en publicidad en TV, radio y periódicos, así como las ventas asociadas. Además, se ha entrenado un modelo de machine learning utilizando estos datos para predecir las ventas en función de los gastos en publicidad.

## Dependencias
El proyecto utiliza las siguientes dependencias:

* Python 3.x
* pandas
* sqlite3
* FastAPI
* uvicorn
Estas dependencias pueden ser instaladas usando pip y el archivo requirements.txt proporcionado.

# Resultados Obtenidos
El proyecto proporciona tres endpoints principales:

* Ingest: Permite ingresar nuevos datos de inversión en publicidad a la base de datos. Se espera que los datos estén en el formato adecuado (TV, radio, periódico, ventas) y se envíen como un diccionario a través de una solicitud POST.
* Predict: Utiliza el modelo de machine learning entrenado para realizar predicciones de ventas en función de los gastos en publicidad. Se espera que los datos de entrada estén en el formato adecuado (TV, radio, periódico) y se envíen como un diccionario a través de una solicitud GET.
* Retrain: Permite reentrenar el modelo de machine learning utilizando los datos existentes en la base de datos. Esto asegura que el modelo esté actualizado con los últimos datos disponibles y puede proporcionar predicciones más precisas.