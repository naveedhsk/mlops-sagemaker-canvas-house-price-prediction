import streamlit as st
import boto3
from botocore.exceptions import ClientError

# --- Streamlit UI ---
st.title("🏠 House Price Predictor - Using SageMaker Canvas")
st.markdown(
    "This app sends data to a deployed SageMaker Canvas endpoint and displays the predicted house price."
)

# Input fields
longitude = st.number_input("Longitude", value=-118.0)
latitude = st.number_input("Latitude", value=34.0)
housing_median_age = st.number_input("Housing Median Age", value=25)
total_rooms = st.number_input("Total Rooms", value=2000)
total_bedrooms = st.number_input("Total Bedrooms", value=400)
population = st.number_input("Population", value=1000)
median_income = st.number_input("Median Income", value=5.0)

# Endpoint name
endpoint_name = "canvas-hp-deployment"

# SageMaker runtime client
client = boto3.client("sagemaker-runtime", region_name="us-east-2")

if st.button("Predict House Price"):
    # --- Create CSV input ---
    csv_input = f"{longitude},{latitude},{housing_median_age},{total_rooms},{total_bedrooms},{population},{median_income}"

    try:
        # Invoke SageMaker endpoint
        response = client.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType="text/csv",
            Body=csv_input
        )

        # Decode the response
        result_str = response["Body"].read().decode().strip()
        #st.write("🔎 Raw model response:")
        #st.code(result_str)

        # Determine if response is numeric
        try:
            predicted_price = float(result_str)
            st.success(f"🏠 Predicted House Price: ${predicted_price:,.0f}")
        except ValueError:
            st.error("❌ Prediction failed: Response is not a valid numeric value.")
            st.json({"response": result_str})

    except ClientError as e:
        error_code = e.response.get("Error", {}).get("Code", "Unknown")
        error_message = e.response.get("Error", {}).get("Message", "No message provided")
        st.error(f"❌ SageMaker Client Error ({error_code}): {error_message}")
        st.write("Please check your endpoint configuration and CloudWatch logs.")
        st.json(e.response)
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {str(e)}")
