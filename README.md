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
