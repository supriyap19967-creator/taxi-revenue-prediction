import os
import joblib
import pandas as pd
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# --------------------
# App initialization
# --------------------
app = FastAPI(title="Taxi Revenue Prediction API")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("taxi-ml-api")

MODEL_VERSION = "v1.0.0"

# --------------------
# Global variables
# --------------------
model = None
features = None

# --------------------
# Input schema
# --------------------
class PredictionRequest(BaseModel):
    pickup_hour: int = Field(..., ge=0, le=23)
    pickup_weekday: int = Field(..., ge=0, le=6)
    trip_count: int = Field(..., ge=0)

    avg_trip_distance: float = Field(..., ge=0)
    avg_trip_duration: float = Field(..., ge=0)
    avg_fare_amount: float = Field(..., ge=0)
    avg_tip_amount: float = Field(..., ge=0)

    payment_2: int = Field(..., ge=0, le=1)
    payment_3: int = Field(..., ge=0, le=1)
    payment_4: int = Field(..., ge=0, le=1)
    payment_5: int = Field(..., ge=0, le=1)

# --------------------
# Startup: load model
# --------------------
@app.on_event("startup")
def load_model():
    global model, features
    base_dir = os.path.dirname(os.path.abspath(__file__))

    model = joblib.load(os.path.join(base_dir, "revenue_rf_model.pkl"))
    features = joblib.load(os.path.join(base_dir, "model_features.pkl"))

    logger.info("Model and features loaded")
    logger.info(f"Model version loaded: {MODEL_VERSION}")

# --------------------
# Health endpoint
# --------------------
@app.get("/")
def health():
    return {
        "status": "ok",
        "model_version": MODEL_VERSION
    }

# --------------------
# Prediction endpoint
# --------------------
@app.post("/predict")
def predict(data: PredictionRequest):
    try:
        logger.info("Prediction request received")

        df = pd.DataFrame([data.dict()])
        df = df.reindex(columns=features, fill_value=0)

        prediction = model.predict(df)[0]

        logger.info("Prediction successful")

        return {
            "model_version": MODEL_VERSION,
            "predicted_total_revenue": round(float(prediction), 2)
        }

    except Exception as e:
        logger.exception("Prediction failed")
        raise HTTPException(
            status_code=500,
            detail="Internal prediction error"
        )
