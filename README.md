# 🏥 Hospital Management System – FastAPI Backend

This is a cloud-native web backend for managing hospital operations such as patients, staff, prescriptions, medications, and medical orders. The system is built using a secure, scalable **three-tier architecture** and modern DevOps practices.

---

## 🔧 Technologies Used

- **FastAPI** – High-performance asynchronous Python framework for REST APIs  
- **JWT Tokens** – Secure, stateless authentication mechanism  
- **SQLAlchemy** – ORM for database modeling and PostgreSQL interaction  
- **Alembic** – Schema migration tool for database evolution  
- **PostgreSQL (Neon)** – Scalable, cloud-hosted relational database  
- **Docker** – Containerization for reproducible and portable deployments  
- **Azure Kubernetes Service (AKS)** – Orchestrates and scales containers  
- **GitHub Actions** – CI/CD pipelines for automated testing and deployment  
- **Postman** – For REST API testing and documentation

---

## 🧱 Architecture & Workflow

The application follows a **three-tier architecture**:

1. **Presentation Layer** – User/client interface  
2. **Application Layer** – FastAPI backend handles logic and authentication  
3. **Data Layer** – PostgreSQL database managed through SQLAlchemy

### Flow:
- Requests are sent to FastAPI
- JWT tokens authenticate access
- SQLAlchemy queries the PostgreSQL database
- The app is containerized with Docker
- CI/CD via GitHub Actions deploys the app to AKS

---

## 🔐 JWT Authentication

- `/login` endpoint returns access token
- Tokens signed with `HS256` algorithm and a secret key
- Middleware validates token for protected routes using `Depends(get_current_user)`

Stateless authentication ensures secure access without storing sessions server-side.

---

## 🧪 API Testing

Test and document all API endpoints via Postman:

🔗 [Hospital API Postman Collection](https://www.postman.com/altimetry-physicist-38912080/my-workspace/collection/vctluhh/robot-spital)

### Features:
- Login and token verification
- Full CRUD for: patients, employees, medications
- Create prescriptions and issue medical orders
- Token error handling (invalid/expired)

---



Api documentation: http://132.220.195.219/docs
