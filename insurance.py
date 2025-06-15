from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_imput import UserInput  # Assuming UserInput is defined in user_input.py
from model.predict import predict_output, model, MODEL_version  # Assuming predict_output and model are defined in predict.py
from schema.prediction_response import PredictionResponse  # Assuming PredictionResponse is defined in prediction_response.py

app = FastAPI()




@app.get('/')
def home():
    return {'message': 'Welcome to the Insurance Premium Prediction API'}

@app.get('/health')
def health_check():
    """
    Health check endpoint to verify if the API is running.
    Returns a simple JSON response indicating the service is up.
    """
    return {
        "message": "API is running",
        "version": MODEL_version,
        "model_loaded": model is not None,
        }

@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):
    """
    Predicts the insurance premium category based on user input.

    The input DataFrame is constructed using the computed fields
    (bmi, age_group, lifestyle_risk, city_tier) and direct inputs
    (income_lpa, occupation) that the 'model.pkl' is expected to
    receive directly for prediction. The order of columns is explicitly
    defined to match the model's training expectations.
    """
    
    # Define the exact order of columns that your model.pkl expects.
    # This order MUST match the order of features used when the model was trained.
    # Based on the previous error message and your training script, these are the columns.
    expected_columns_for_model = [
        'bmi',
        'age group', # Changed from 'age_group' to 'age group' to match training script
        'lifestyle_risk',
        'city_tier',
        'income_lpa',
        'occupation'
    ]

    # Create a dictionary of the values, using the computed properties from 'data'
    User_input = {
        'bmi': data.bmi,
        'age group': data.age_group, # Changed from 'age_group' to 'age group'
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    

    try:
        # Perform prediction using the loaded model
        prediction = predict_output(User_input)
        return JSONResponse(status_code=200, content={'predicted_category': prediction})
    except Exception as e:
        # Catch any exceptions during prediction to provide more specific error messages
        return JSONResponse(status_code=500, content={"message": f"Prediction error: {e}"})
