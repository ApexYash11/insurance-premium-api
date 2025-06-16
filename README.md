🧠 Insurance Premium Prediction API
An end-to-end MLOps project that predicts the insurance premium category based on user input using a trained machine learning model. It features both an interactive frontend (Streamlit) and an API backend (FastAPI), all containerized with Docker.

📦 Tech Stack
Machine Learning: Scikit-learn

Backend API: FastAPI

Frontend UI: Streamlit

Deployment: Docker, AWS EC2

Visualization: Swagger (via FastAPI)

🚀 How to Run Locally
1. Clone this repository
git clone https://github.com/ApexYash11/insurance-premium-api.git
cd insurance-premium-api

2. (Optional) Create and activate a virtual environment
python -m venv env
env\Scripts\activate # Windows
source env/bin/activate # macOS/Linux

3. Install dependencies
pip install -r requirements.txt

4. Run the FastAPI backend
python insurance.py

Go to: http://51.20.254.126:8000/docs for Swagger UI

5. Run the Streamlit frontend
streamlit run frontend.py

🐳 Docker Setup
Build the Docker image
docker build -t insurance-api .

Run the Docker container
docker run -p 8000:8000 insurance-api

🌐 Live Deployment
🔗 Streamlit App: https://insurance-premium-api.streamlit.app/

🐳 DockerHub Repo: https://hub.docker.com/repositories/apexyash11

📝 License
This project is licensed under the MIT License

👨‍💻 Author
Made with ❤️ by Yash Maheshwari
Cheers to many more projects and learnings!
