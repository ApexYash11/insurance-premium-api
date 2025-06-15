import pickle
import pandas as pd

# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_version= "1.0.0"  # Version of the model, can be used for logging or tracking purposes    

 # Get the class labels from the model 
class_labels =model.classes_.tolist() 

def predict_output(user_input : dict):
    input_df=pd.DataFrame([user_input])

    #predict class 
    predict_class = model.predict(input_df)[0]

    # get probabalites for all classes
    probabilities = model.predict_proba(input_df)[0]
    confidence=max(probabilities)

    # creating mapping : (class_name:probability)
    class_probs =dict(zip(class_labels, map(lambda x: round(x, 2), probabilities)))
   
    return {
        "predicted_category": predict_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }
    
    