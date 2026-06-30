# AI Health Triage Assistant

AI Health Triage Assistant is a web-based triage and decision-support app that helps users describe symptoms, receive likely condition matches, understand urgency, and prepare a doctor-ready consultation summary.

This project is designed for a hackathon-style end-to-end healthcare workflow: symptom intake, deterministic ML prediction, LLM-assisted explanation, urgency scoring, report generation, and consultation history.

> Disclaimer: This product is not a medical diagnosis tool and does not replace professional medical advice. Users should always consult a qualified doctor for confirmation and treatment.

## Features

- Symptom intake flow with searchable symptoms and basic patient details.
- Top-3 predicted conditions with confidence scores.
- Matched-symptom explanation for more transparent predictions.
- Urgency levels: Green, Yellow, Orange, and Red.
- Patient-friendly explanation and next-step guidance.
- Doctor-ready report download from the frontend.
- Consultation history view.
- FastAPI backend with health and authentication routes.
- Planned ML service for disease prediction from structured symptoms.
- Planned Lemma SDK workflow for consultation persistence and judging deployment.

## Current Status

The repository currently contains:

- A Next.js frontend with the landing page, consultation flow, history page, local mock prediction data, and PDF report download behavior.
- A FastAPI backend scaffold with configuration, database models, repositories, services, authentication routes, and a health route.
- Alembic setup for database migrations.
- An empty `ml-service` scaffold that is intended to host the trained symptom-to-disease model.
- Setup and data scripts under `scripts/`.

Some blueprint features are still in progress, including the trained ML model artifact, live backend prediction endpoints, Gemini explanation integration, Lemma SDK orchestration, and production deployment.

## Tech Stack

| Layer | Technology |
| --- | --- |
| Frontend | Next.js, React, TypeScript, Tailwind CSS, shadcn/ui |
| Backend | FastAPI, Pydantic, SQLAlchemy, Alembic |
| Database | PostgreSQL |
| ML | scikit-learn / XGBoost planned |
| LLM | Gemini Flash planned for explanation and report text |
| Workflow | Lemma SDK planned |
| Reports | Frontend PDF report generation currently implemented |

## Project Structure

```text
.
+-- backend/
|   +-- alembic/
|   +-- app/
|       +-- api/
|       +-- core/
|       +-- database/
|       +-- models/
|       +-- repositories/
|       +-- schemas/
|       +-- services/
+-- frontend/
|   +-- app/
|   +-- components/
|   +-- hooks/
|   +-- lib/
|   +-- public/
|   +-- styles/
+-- ml-service/
+-- scripts/
+-- docker-compose.yml
+-- README.md
```

## Getting Started

### Prerequisites

- Node.js 20+ recommended
- Python 3.11+ recommended
- PostgreSQL
- npm or pnpm

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend runs at:

```text
http://localhost:3000
```

Useful commands:

```bash
npm run build
npm run start
npm run lint
```

### Backend

Create a backend virtual environment and install dependencies:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Create `backend/.env`:

```env
APP_NAME=AI Health Triage Assistant
APP_VERSION=1.0.0
DEBUG=true
HOST=0.0.0.0
PORT=8000
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/ai_health_triage
SECRET_KEY=change-this-secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Run migrations:

```bash
alembic upgrade head
```

Start the API:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend runs at:

```text
http://localhost:8000
```

OpenAPI docs are available at:

```text
http://localhost:8000/docs
```

## API Surface

Implemented routes currently include:

| Method | Route | Description |
| --- | --- | --- |
| GET | `/` | Backend root status |
| GET | `/api/v1/health/` | API health check |
| POST | `/api/v1/auth/register` | Register a user |
| POST | `/api/v1/auth/login` | Log in and receive a token |

Blueprint/planned routes include:

| Method | Route | Description |
| --- | --- | --- |
| POST | `/api/v1/predict` | Return top-3 disease predictions from symptoms |
| POST | `/api/v1/explain` | Generate patient-friendly explanation text |
| POST | `/api/v1/consultation` | Persist a full consultation workflow |
| GET | `/api/v1/history` | Fetch consultation history |
| GET | `/api/v1/report/{id}` | Fetch a generated doctor report |

## Intended Workflow

1. User selects symptoms and enters basic intake details.
2. Backend sends structured symptoms to the ML prediction service.
3. The ML model returns top-3 likely conditions with confidence scores.
4. The LLM explains the ML output in plain language without changing the prediction.
5. The urgency service assigns Green, Yellow, Orange, or Red.
6. The report service creates a doctor-ready summary.
7. The consultation is saved to history through the Lemma SDK workflow.

## Machine Learning Plan

The model pipeline is intended to use the Kaggle Disease and Symptoms dataset:

- Normalize symptom names.
- Remove duplicates and handle missing values.
- Build a canonical symptom vocabulary.
- One-hot encode symptoms.
- Train and compare Random Forest and XGBoost classifiers.
- Return top-3 predictions with confidence scores.
- Export the best model as a `.pkl` artifact for service loading.

The LLM should never perform disease prediction directly. It should only explain, summarize, and recommend next steps based on deterministic model output.

## Roadmap

- Add the trained ML model and prediction endpoint.
- Connect the frontend consultation flow to FastAPI.
- Add Gemini Flash explanation service.
- Implement urgency rules in the backend.
- Persist consultation history in PostgreSQL.
- Generate backend PDF reports.
- Integrate the Lemma SDK workflow.
- Complete Docker Compose for local full-stack startup.
- Deploy frontend, backend, database, and Lemma pod.

## Hackathon Deliverables

- Working hosted web app.
- GitHub repository with this README.
- Demo video.
- Architecture diagram / project blueprint.
- Model evaluation metrics.
- Final submission write-up.

## License

Add a license before publishing or submitting the repository publicly.
