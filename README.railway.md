# Todo API - Railway Deployment

This is a FastAPI-based Todo application ready for deployment on Railway.

## Deploying to Railway

### Option 1: One-Click Deploy
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/your-username/todo-app/tree/main/backend)

### Option 2: Manual Deployment
1. Install the [Railway CLI](https://docs.railway.app/cli/installation)
2. Login: `railway login`
3. Link your project: `railway init`
4. Set environment variables:
   - `DATABASE_URL`: Your PostgreSQL database connection string
   - `ALLOWED_ORIGINS`: Comma-separated list of allowed origins (defaults to "*")
5. Deploy: `railway deploy`

## Environment Variables

- `DATABASE_URL`: PostgreSQL database connection string (required)
- `ALLOWED_ORIGINS`: Comma-separated list of allowed origins for CORS (optional, defaults to "*")

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/tasks` - Retrieve all tasks
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/{id}` - Retrieve a specific task
- `PUT /api/tasks/{id}` - Update a specific task
- `DELETE /api/tasks/{id}` - Delete a specific task
- `PATCH /api/tasks/{id}/status` - Update task status

## Database Setup

This application supports both SQLite (for development) and PostgreSQL (recommended for production). When deploying to Railway, it's recommended to use Railway's PostgreSQL addon.

## Notes

- The application listens on the port specified by the `PORT` environment variable (defaults to 8000)
- CORS is enabled for all origins by default (configure ALLOWED_ORIGINS for production)
- The application automatically handles the difference between `postgres://` and `postgresql://` URLs