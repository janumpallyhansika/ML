import streamlit as st
import pandas as pd
import joblib

ridge_model = joblib.load(
    "ridge_travel_time_model.pkl"
)

lasso_model = joblib.load(
    "lasso_travel_time_model.pkl"
)

st.set_page_config(
    page_title="Travel Time Prediction",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Travel Time Prediction")
st.subheader("Using Ridge and Lasso Regression")

st.write(
    "Enter the traffic and environmental conditions "
    "to predict travel time."
)

st.divider()

city_zone = st.selectbox(
    "City Zone",
    [
        "Commercial",
        "Residential",
        "Downtown",
        "Suburban",
        "Industrial"
    ]
)

road_type = st.selectbox(
    "Road Type",
    [
        "Highway",
        "Local Road",
        "Main Road"
    ]
)

traffic_volume = st.number_input(
    "Traffic Volume",
    min_value=0,
    value=2000
)

average_speed_kmph = st.number_input(
    "Average Speed (km/h)",
    min_value=1.0,
    value=40.0
)

weather_condition = st.selectbox(
    "Weather Condition",
    [
        "Clear",
        "Rain",
        "Storm",
        "Fog"
    ]
)

accident_reported = st.selectbox(
    "Accident Reported",
    [
        "No",
        "Yes"
    ]
)

congestion_level = st.selectbox(
    "Congestion Level",
    [
        "Low",
        "Medium",
        "High"
    ]
)

hour = st.slider(
    "Hour of Day",
    0,
    23,
    18
)

day_of_week = st.slider(
    "Day of Week",
    0,
    6,
    0
)

month = st.slider(
    "Month",
    1,
    12,
    1
)

is_weekend = st.selectbox(
    "Is Weekend?",
    [0, 1],
    format_func=lambda x:
    "Yes" if x == 1 else "No"
)

if st.button(
    "Predict Travel Time",
    type="primary"
):

    input_data = pd.DataFrame({
        "city_zone": [city_zone],
        "road_type": [road_type],
        "traffic_volume": [traffic_volume],
        "average_speed_kmph": [
            average_speed_kmph
        ],
        "weather_condition": [
            weather_condition
        ],
        "accident_reported": [
            accident_reported
        ],
        "congestion_level": [
            congestion_level
        ],
        "hour": [hour],
        "day_of_week": [day_of_week],
        "month": [month],
        "is_weekend": [is_weekend]
    })

    ridge_prediction = (
        ridge_model.predict(input_data)[0]
    )

    lasso_prediction = (
        lasso_model.predict(input_data)[0]
    )

    st.success(
        "Prediction completed!"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Ridge Prediction",
            f"{ridge_prediction:.2f} minutes"
        )

    with col2:
        st.metric(
            "Lasso Prediction",
            f"{lasso_prediction:.2f} minutes"
        )