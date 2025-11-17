# Analyze - Comprehensive Data Analysis Service

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)

Analyze is an enterprise-grade data analysis service built with FastAPI that provides comprehensive statistical analysis, visualization generation, and automated reporting capabilities. Inspired by modern AI-powered development workflows, this project demonstrates a clean, service-oriented architecture for handling complex data analysis tasks.

## ✨ Key Features

- **RESTful API Architecture**: Built with FastAPI for high performance and automatic API documentation
- **Comprehensive Data Analysis**: Supports descriptive statistics, correlation analysis, and advanced analytics
- **Automated Visualizations**: Generate publication-ready charts and graphs automatically
- **Async Processing**: Non-blocking task execution with background processing capabilities
- **Type Safety**: Full type hints throughout the codebase using modern Python typing
- **Production-Ready**: Structured logging, error handling, and CORS configuration
- **Docker Support**: Containerized deployment for easy scaling and deployment

## 🏗️ Architecture

The project follows a clean, modular architecture:

```
Analyze/
├── src/
│   └── analyzer/
│       ├── __init__.py
│       └── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

### Technology Stack

| Component | Technology |
|-----------|------------|
| **Framework** | FastAPI, Uvicorn |
| **Data Processing** | Pandas, NumPy, SciPy |
| **Machine Learning** | Scikit-learn |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Database** | SQLAlchemy, Alembic |
| **Testing** | Pytest, Pytest-asyncio |

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/IITM-SMRITHI/Analyze.git
   cd Analyze
   ```

2. **Create and activate a virtual environment**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   cd src/analyzer
   python main.py
   ```

The server will start at `http://localhost:8000`

## 📖 API Documentation

Once the server is running, visit:
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

### API Endpoints

#### Health Check
```bash
GET /
```
Returns service status and version information.

#### Submit Analysis Task
```bash
POST /api/analyze
Content-Type: application/json

{
  "email": "23f3004253@ds.study.iitm.ac.in",
  "dataset_name": "sales_data",
  "analysis_type": "comprehensive",
  "include_visualization": true
}
```

#### Check Task Status
```bash
GET /api/status/{task_id}
```

#### Get Statistics
```bash
GET /statistics
```

## 🎯 Usage Examples

### Example 1: Basic Analysis Request

```bash
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "email": "23f3004253@ds.study.iitm.ac.in",
    "dataset_name": "customer_data",
    "analysis_type": "descriptive",
    "include_visualization": true
  }'
```

### Example 2: Using Python Requests

```python
import requests

response = requests.post(
    "http://localhost:8000/api/analyze",
    json={
        "email": "23f3004253@ds.study.iitm.ac.in",
        "dataset_name": "sales_data",
        "analysis_type": "comprehensive",
        "include_visualization": True
    }
)

print(response.json())
```

## 🔧 Configuration

The application can be configured through environment variables:

```bash
# Server Configuration
HOST=0.0.0.0
PORT=8000

# Logging
LOG_LEVEL=INFO

# CORS
ALLOWED_ORIGINS=*
```

## 🐳 Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

EXPOSE 8000

CMD ["python", "src/analyzer/main.py"]
```

Build and run:

```bash
docker build -t analyze-service .
docker run -p 8000:8000 analyze-service
```

## 🧪 Testing

Run tests using pytest:

```bash
pytest
```

With coverage:

```bash
pytest --cov=src --cov-report=html
```

## 📊 Project Status

- ✅ Core FastAPI application
- ✅ REST API endpoints
- ✅ Data models with Pydantic
- ✅ Error handling and logging
- ⏳ Database integration
- ⏳ Advanced analytics features
- ⏳ Comprehensive test suite
- ⏳ CI/CD pipeline

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**IITM-SMRITHI**
- Email: [23f3004253@ds.study.iitm.ac.in](mailto:23f3004253@ds.study.iitm.ac.in)
- GitHub: [@IITM-SMRITHI](https://github.com/IITM-SMRITHI)

## 🙏 Acknowledgments

- Inspired by modern AI-powered development workflows
- Built for the TDS (Tools in Data Science) course
- Reference architecture from [brahmacode](https://github.com/mynkpdr/brahmacode)

## 📮 Contact

For questions or feedback, please reach out to: **23f3004253@ds.study.iitm.ac.in**

---

**Made with ❤️ by IITM-SMRITHI for the IIT Madras Data Science Program**
