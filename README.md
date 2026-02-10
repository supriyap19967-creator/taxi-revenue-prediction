####Taxi Revenue Prediction – Production ML API (GCP)####

End-to-end production machine learning API to predict taxi revenue from structured trip data.
Built with MLOps practices and deployed on Google Cloud Run.

## Live API
Base URL:
https://taxi-ml-api-202553701738.us-central1.run.app

Swagger UI:
https://taxi-ml-api-202553701738.us-central1.run.app/docs

## Architecture
Offline training → Model artifact (.pkl) → FastAPI inference service → Cloud Run

## Tech Stack
- Python
- Scikit-learn (Random Forest)
- FastAPI
- Pydantic
- Docker
- Google Cloud Run

## Data Engineering
- Designed relational schema for taxi trip, fare, and location data
- Built analytical SQL views on raw trip data using SQLite
- Derived time-based features (hour, weekday) from timestamps
- Created aggregated features using SQL (counts, averages, revenue sums)
- Produced ML-ready analytical views for downstream model training


## Machine Learning
- Revenue prediction using supervised regression
- Feature engineering with aggregated trip statistics and encoded payment types
- Baseline modeling with Linear Regression and final model selection using Random Forest
- Model evaluation using Mean Absolute Error (MAE)
- Trained model and feature schema serialized for production inference


## MLOps Practices
- Training vs serving separation
- Input schema validation
- Error handling
- Structured logging
- Model versioning
- Health endpoint
- Safe cloud deployment

## API

# Health
GET /

Response:
```json
{
  "status": "ok",
  "model_version": "v1.0.0"
}

