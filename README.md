# mlops-sagemaker-canvas-house-price-prediction

Welcome to the mlops-sagemaker-canvas-house-price-prediction wiki!

A lightweight app that predicts house prices using a model deployed in AWS SageMaker Canvas. Built with Streamlit and integrated with AWS SDK to securely connect to the endpoint.









🚀 Features





Simple and interactive UI with Streamlit
Real-time predictions from SageMaker Canvas endpoint
AWS best practices: endpoint invocation without exposing credentials
📷 Visual example of the UI below!










🌟 Project Overview





This project demonstrates how to deploy a machine learning model using SageMaker Canvas and connect it to a Python web app using Streamlit. The app sends user-provided features to the model endpoint and displays the predicted house price.









🛠️ Tech Stack





Python (Streamlit, Boto3)
AWS SageMaker Canvas
AWS IAM roles / instance profiles
Deployed on AWS EC2 / local machine










📝 Setup & Run





1️⃣ Clone the repo:

git clone https://github.com/naveedhsk/mlops-sagemaker-canvas-house-price-prediction.git

cd house-price-prediction-sagemaker-canvas

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Run the app:

streamlit run app.py









📷 UI Screenshot



  









💡 Learnings & Challenges





✅ Working with CSV input format for SageMaker Canvas

✅ Handling JSON vs plain text responses

✅ Secure AWS access using instance profiles instead of static credentials

✅ Smooth UX with Streamlit for real-time feedback









🎯 My Professional Take





As an aspiring MLOps / ML Platform Engineer, I see this as an essential pattern for model deployment and real-time serving. Canvas is great for rapid ML iteration, and this project shows how to take those models into production with clean, maintainable code.









🤝 Connect with Me





🔗 [LinkedIn](https://www.linkedin.com/in/naveedh-sk/)

