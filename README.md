# VulnFinBot – Secure CI/CD Pipeline

## 1. Project Description

VulnFinBot is a simple Flask-based financial chatbot API created for a laboratory project.

The project demonstrates how to build a secure CI/CD pipeline with automated testing and security scanning.

## 2. Technologies Used

- Python 3.12
- Flask
- Pytest
- GitHub Actions
- Bandit – Static Application Security Testing (SAST)
- Semgrep – Static code analysis
- pip-audit – Dependency vulnerability scanning
- Docker – Application containerization
- Trivy – Docker image vulnerability scanning
- OWASP ZAP – Dynamic Application Security Testing (DAST)

## 3. Project Structure

```text
app/                  Flask application
tests/                API and AI security tests
security/semgrep/     Custom Semgrep rules
reports/              Security reports
.github/workflows/    GitHub Actions pipeline
Dockerfile            Docker configuration
requirements.txt      Python dependencies
run.py                Application entry point
```

## 4. API Endpoints

### GET /health

Checks application availability.

Example response:

```json
{
  "status": "healthy"
}
```

### POST /api/chat

Accepts a JSON message and returns a response.

Example request:

```json
{
  "message": "Hello"
}
```

## 5. Security Testing

The pipeline performs:

- Unit and API testing with Pytest.
- AI security scenario testing.
- Static code analysis with Bandit and Semgrep.
- Dependency scanning with pip-audit.
- Docker image scanning with Trivy.
- Dynamic application scanning with OWASP ZAP.

AI security tests cover instruction override, system prompt disclosure, sensitive data disclosure, unauthorized tool usage, and output validation.

**Note:** AI security tests use predefined API responses and simulate security scenarios. They do not evaluate a real language model.

## 6. CI/CD Pipeline

GitHub Actions automatically runs the pipeline when code is pushed to the main branch or a pull request is created.

The pipeline:

1. Installs dependencies.
2. Runs automated tests.
3. Performs SAST scans.
4. Checks dependencies for known vulnerabilities.
5. Builds the Docker image.
6. Scans the image with Trivy.
7. Runs OWASP ZAP DAST scanning.
8. Uploads security reports as workflow artifacts.

## 7. Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -v
```

Start the application:

```bash
python run.py
```

Open:

```text
http://127.0.0.1:5000/health
```

## 8. Docker

Build the image:

```bash
docker build -t vulnfinbot:latest .
```

Run the container:

```bash
docker run -d -p 5000:5000 vulnfinbot:latest
```

## 9. Security Reports

The GitHub Actions workflow generates reports for:

- Pytest results
- Bandit
- Semgrep
- pip-audit
- Trivy
- OWASP ZAP JSON and HTML reports

Reports are uploaded as the `security-reports` artifact.

## 10. Conclusion

This project demonstrates an automated security-focused CI/CD pipeline for a Flask application. It combines application testing, static analysis, dependency scanning, container security, and dynamic security testing.