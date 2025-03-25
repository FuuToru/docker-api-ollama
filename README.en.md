# Docker API Ollama

A lightweight Dockerized application integrating FastAPI and Ollama for sentiment analysis of text. The project uses the `llama3.2:1b` model to classify sentiments into three categories: Neutral (NEU), Positive (POS), and Negative (NEG).

## Project Structure

```
fuutoru-docker-api-ollama/
├── docker-compose.yml         # Docker Compose configuration
├── fastapi/                   # FastAPI service directory
│   ├── app.py                 # Main FastAPI application
│   ├── Dockerfile             # Dockerfile for FastAPI service
│   └── requirements.txt       # Python dependencies
└── ollama/                    # Ollama service directory
    ├── Dockerfile             # Dockerfile for Ollama service
    └── pull-llama3.sh         # Script to pull and run llama3.2:1b model
```

## Features

- **Sentiment Analysis**: Analyzes text input to determine sentiment (NEU, POS, NEG) using the `llama3.2:1b` model.
- **Dockerized Services**: Runs FastAPI and Ollama in isolated containers for easy deployment and scalability.
- **API Endpoint**: Provides a simple GET endpoint (`/ask`) to process text and return sentiment labels.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/fuutoru-docker-api-ollama.git
   cd fuutoru-docker-api-ollama
   ```

2. **Build and run the services**:
   ```bash
   docker-compose up --build
   ```
   This command builds the FastAPI and Ollama images and starts the containers. The Ollama service will automatically pull the `llama3.2:1b` model on the first run.

3. **Verify the services**:
   - FastAPI will be available at `http://localhost:8000`.
   - Ollama will be available at `http://localhost:11434`.

## Usage

### API Endpoints

1. **Health Check**:
   - **Endpoint**: `GET /`
   - **Response**: `{"status": "Ok"}`
   - **Description**: Checks if the FastAPI service is running.

   Example:
   ```bash
   curl http://localhost:8000/
   ```

2. **Sentiment Analysis**:
   - **Endpoint**: `GET /ask?prompt=<your-text>`
   - **Response**: One of `NEU`, `POS`, or `NEG`
   - **Description**: Analyzes the sentiment of the provided text.

   Example:
   ```bash
   curl "http://localhost:8000/ask?prompt=rất%20tuyệt%20vời"
   ```
   Response: `POS`

### Example Scenarios

- Input: `"hoạt động kém hiệu quả"`
  - Output: `NEG`
- Input: `"Tôi không có ý kiến gì"`
  - Output: `NEU`
- Input: `"đang phát triển mạnh mẽ"`
  - Output: `POS`

## Configuration

- **Ports**:
  - FastAPI: `8000`
  - Ollama: `11434`
- **Volumes**:
  - FastAPI source code is mounted for live reloading during development.
  - Ollama persists model data in the `ollama_volume` Docker volume.

## Development

To modify the FastAPI application:
1. Edit `fastapi/app.py`.
2. Changes will be reloaded automatically due to the `--reload` flag in the FastAPI Dockerfile.

To use a different model:
1. Update the `model` field in `fastapi/app.py` (e.g., replace `llama3.2:1b` with another model).
2. Modify `ollama/pull-llama3.sh` to pull the desired model.

## Troubleshooting

- **Service not starting**: Check Docker logs with `docker-compose logs`.
- **Model not loading**: Ensure internet access for the Ollama container to pull the `llama3.2:1b` model.
- **API errors**: Verify the Ollama service is running and accessible at `http://ollama:11434`.

## Contributing

Feel free to submit issues or pull requests to improve this project. Please follow standard GitHub workflows for contributions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the web framework.
- [Ollama](https://ollama.ai/) for providing the `llama3.2:1b` model and runtime.

