# ============================================================

# PART 1: IMPORTS, PAGE CONFIGURATION AND PREMIUM CSS

# ============================================================



import time
import textwrap

from datetime import date

from pathlib import Path

from urllib.parse import quote



import joblib

import numpy as np

import pandas as pd

import requests

import streamlit as st

import folium

from streamlit_folium import st_folium





# ============================================================

# PAGE CONFIGURATION

# ============================================================



st.set_page_config(

    page_title="TravelTime AI",

    page_icon="🚗",

    layout="wide",

    initial_sidebar_state="collapsed"

)





# ============================================================

# PREMIUM SOFT-COLOUR CSS

# ============================================================



st.markdown("\n".join(line.lstrip() for line in textwrap.dedent("""

<style>

:root {

    --ink: #49364F;

    --muted: #817487;

    --plum: #9B78AA;

    --rose: #D58FA9;

    --cream: #FFF9F4;

    --line: #E9DDEA;

}



/* Layered luxury background */

.stApp {

    background:

        radial-gradient(

            ellipse at 7% 7%,

            rgba(244, 207, 222, .75) 0%,

            transparent 30%

        ),

        radial-gradient(

            ellipse at 92% 15%,

            rgba(218, 211, 245, .75) 0%,

            transparent 32%

        ),

        radial-gradient(

            ellipse at 85% 95%,

            rgba(255, 222, 198, .58) 0%,

            transparent 30%

        ),

        linear-gradient(

            135deg,

            #FFF9F4 0%,

            #F9F1F8 52%,

            #F0F0FC 100%

        );

    color: var(--ink);

}



.block-container {

    max-width: 1380px;

    padding: 2.3rem 2.5rem 3.5rem;

}



#MainMenu,

footer {

    visibility: hidden;

}



header[data-testid="stHeader"] {

    background: transparent;

}



/* Typography */

h1, h2, h3 {

    color: var(--ink) !important;

    font-weight: 780 !important;

    letter-spacing: -.65px;

}



h1 {

    font-size: clamp(2rem, 3vw, 2.8rem) !important;

}



h2 {

    font-size: 2rem !important;

}



h3 {

    font-size: 1.35rem !important;

}



p,

.stCaption {

    color: var(--muted) !important;

}



/* Login heading */

.login-title {

    color: #49364F;

    font-size: clamp(2.1rem, 3vw, 2.8rem);

    line-height: 1.12;

    font-weight: 850;

    letter-spacing: -1.2px;

    margin: .5rem 0 .65rem;

}



.login-title::before {

    content: "TRAVELTIME AI / SMART JOURNEYS";

    display: block;

    width: fit-content;

    margin-bottom: 1.15rem;

    padding: 8px 13px;

    border-radius: 999px;

    background: linear-gradient(

        100deg,

        #F5E2EB,

        #EAE4F7

    );

    border: 1px solid rgba(190, 157, 198, .25);

    color: #886A96;

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1.25px;

}



.login-description {

    color: #88798D;

    font-size: 15px;

    line-height: 1.7;

    margin-bottom: 1.25rem;

}



/* Travel image */

.stImage img {

    border-radius: 26px;

    border: 5px solid rgba(255, 255, 255, .78);

    box-shadow: 0 24px 55px rgba(93, 65, 103, .18);

    transition:

        transform .25s ease,

        box-shadow .25s ease;

}



.stImage img:hover {

    transform: translateY(-3px);

    box-shadow: 0 30px 65px rgba(93, 65, 103, .23);

}



/* Form labels */

.stTextInput label,

.stSelectbox label,

.stDateInput label,

.stSlider label,

.stNumberInput label {

    color: #66556D !important;

    font-size: 13px !important;

    font-weight: 700 !important;

}



/* Text inputs */

.stTextInput input,

.stDateInput input,

.stNumberInput input,

.stTextArea textarea {

    background: rgba(255, 255, 255, .9) !important;

    color: #49364F !important;

    border: 1px solid #E6D9E9 !important;

    border-radius: 13px !important;

    min-height: 48px !important;

    font-size: 14px !important;

    box-shadow: 0 4px 14px rgba(92, 65, 100, .045);

    transition:

        border-color .2s ease,

        box-shadow .2s ease;

}



.stTextInput input:focus,

.stDateInput input:focus,

.stNumberInput input:focus,

.stTextArea textarea:focus {

    border-color: #B18ABB !important;

    box-shadow: 0 0 0 3px rgba(177, 138, 187, .15) !important;

}



.stTextInput input::placeholder {

    color: #B1A5B7 !important;

}



/* Dropdowns */

div[data-baseweb="select"] > div {

    background: rgba(255, 255, 255, .92) !important;

    border: 1px solid #E6D9E9 !important;

    border-radius: 13px !important;

    min-height: 48px !important;

}



div[data-baseweb="select"] span {

    color: #49364F !important;

}



/* Buttons */

.stButton > button,

.stFormSubmitButton > button,

.stLinkButton > a {

    background: linear-gradient(

        112deg,

        #9B78AA 0%,

        #C58EAD 100%

    ) !important;

    color: #FFFFFF !important;

    border: 1px solid rgba(255, 255, 255, .5) !important;

    border-radius: 13px !important;

    min-height: 48px !important;

    font-weight: 750 !important;

    box-shadow: 0 9px 22px rgba(153, 111, 166, .23);

    transition:

        transform .2s ease,

        box-shadow .2s ease;

}



.stButton > button:hover,

.stFormSubmitButton > button:hover,

.stLinkButton > a:hover {

    transform: translateY(-2px);

    box-shadow: 0 13px 27px rgba(153, 111, 166, .3);

}



/* Prediction button */

.predict-button-container .stButton > button {

    background: linear-gradient(

        105deg,

        #8F6BA2,

        #D18CA8

    ) !important;

    min-height: 54px !important;

    font-size: 16px !important;

    letter-spacing: .15px;

}



/* Ridge and Lasso metric cards */

div[data-testid="stMetric"] {

    background: linear-gradient(

        145deg,

        rgba(255, 255, 255, .96),

        rgba(250, 241, 250, .94)

    );

    border: 1px solid rgba(231, 215, 235, .95);

    border-radius: 20px;

    padding: 22px;

    box-shadow: 0 12px 30px rgba(91, 64, 101, .075);

}



div[data-testid="stMetricLabel"] {

    color: #8B7892 !important;

}



div[data-testid="stMetricValue"] {

    color: #684B78 !important;

    font-size: 29px !important;

    font-weight: 850 !important;

}



/* Content cards */

.info-card,

.route-card {

    background: rgba(255, 255, 255, .78);

    border: 1px solid rgba(255, 255, 255, .95);

    border-radius: 22px;

    padding: 20px;

    box-shadow: 0 12px 32px rgba(91, 64, 101, .08);

}



.route-card {

    padding: 10px;

}



/* Tabs */

.stTabs [data-baseweb="tab-list"] {

    gap: 8px;

    background: rgba(255, 255, 255, .58);

    border: 1px solid rgba(231, 215, 235, .8);

    padding: 7px;

    border-radius: 15px;

}



.stTabs [data-baseweb="tab"] {

    border-radius: 10px;

    color: #7C6A83;

}



.stTabs [aria-selected="true"] {

    background: linear-gradient(

        100deg,

        #F1E3F4,

        #F8E4EC

    ) !important;

    color: #684B78 !important;

}



/* Alerts and expanders */

div[data-testid="stExpander"],

div[data-testid="stAlert"] {

    border-radius: 15px;

    border-color: #E8D9EB;

}



/* Dividers */

hr {

    border-color: rgba(218, 202, 224, .8) !important;

}



/* Sidebar */

section[data-testid="stSidebar"] {

    background: linear-gradient(

        180deg,

        #F4E8F4,

        #FFF5EF

    );

    border-right: 1px solid #E8D9EB;

}



/* Responsive layout */

@media (max-width: 768px) {

    .block-container {

        padding: 1.2rem .85rem 2rem;

    }



    .login-title {

        font-size: 2rem;

    }



    .stImage img {

        border-radius: 18px;

    }

}

</style>

""").splitlines()), unsafe_allow_html=True)





# END OF PART 1

# Continue by pasting Part 2 below this line.



# ============================================================

# PART 2: SESSION STATE, MODEL LOADING, LOGIN AND LOGOUT

# ============================================================



# SESSION STATE

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False



if "prediction" not in st.session_state:

    st.session_state.prediction = None



if "pickup_location" not in st.session_state:

    st.session_state.pickup_location = ""



if "drop_location" not in st.session_state:

    st.session_state.drop_location = ""





# ============================================================

# LOAD TRAINED MODELS

# ============================================================



MODEL_FILE = (

    Path(__file__).resolve().parent

    / "travel_time_models.pkl"

)



try:

    bundle = joblib.load(MODEL_FILE)



except Exception as error:

    st.error("Could not load travel_time_models.pkl")

    st.info(

        "Keep travel_time_models.pkl in the same folder as app.py."

    )

    st.stop()





try:

    ridge_model = bundle["ridge_model"]

    lasso_model = bundle["lasso_model"]



except Exception:

    st.error(

        "The model file must contain both Ridge and Lasso models."

    )

    st.stop()





FEATURES = bundle.get(

    "features",

    [

        "start_lng",

        "start_lat",

        "end_lng",

        "end_lat",

        "distance_km",

        "hour",

        "day_of_week",

        "month",

        "is_weekend",

    ],

)



RIDGE_MAE = float(bundle.get("ridge_mae", 0))

LASSO_MAE = float(bundle.get("lasso_mae", 0))





# ============================================================

# LOGIN PAGE

# ============================================================



def login_page():



    left, right = st.columns(

        [1.15, 0.85],

        gap="large"

    )



    # LEFT SIDE: TRAVEL IMAGE AND BRANDING

    with left:



        st.write("")



        st.image(

            "https://images.unsplash.com/"

            "photo-1464822759023-fed622ff2c3b"

            "?auto=format&fit=crop&w=1400&q=90",

            use_container_width=True

        )



        st.markdown(

            "### TravelTime AI"

        )



        st.caption(

            "Intelligent travel-time prediction "

            "for smarter journeys."

        )



        with st.container(border=True):
            st.markdown("**YOUR JOURNEY, REIMAGINED**")
            st.caption(
                "Plan your route, compare travel-time predictions, "
                "and make more informed journey decisions."
            )



    # RIGHT SIDE: LOGIN FORM

    with right:



        st.write("")

        st.write("")

        st.write("")



        st.markdown(

            '<div class="login-title">Welcome back</div>',

            unsafe_allow_html=True

        )



        st.markdown(

            '<div class="login-description">'

            'Sign in to plan your next journey.'

            '</div>',

            unsafe_allow_html=True

        )



        st.write("")



        with st.container(border=True):



            st.markdown("#### Sign in to your account")



            email = st.text_input(

                "Email",

                placeholder="Enter your email",

                key="login_email"

            )



            password = st.text_input(

                "Password",

                type="password",

                placeholder="Enter your password",

                key="login_password"

            )



            st.write("")



            if st.button(

                "Sign In  →",

                use_container_width=True,

                key="login_button"

            ):



                # Existing local demo credentials

                if (

                    email.strip().lower()

                    == "janumpallyhansika@gmail.com"

                    and password == "Travel@123"

                ):



                    st.session_state.logged_in = True

                    st.session_state.prediction = None



                    st.rerun()



                else:

                    st.error(

                        "Invalid email or password."

                    )



            st.write("")



            st.caption(

                "Secure access to your travel prediction dashboard."

            )





# ============================================================

# SWAP PICKUP AND DROP-OFF LOCATIONS

# ============================================================



def swap_locations():



    pickup = st.session_state.get(

        "pickup_location",

        ""

    )



    drop = st.session_state.get(

        "drop_location",

        ""

    )



    st.session_state["pickup_location"] = drop

    st.session_state["drop_location"] = pickup





# ============================================================

# LOGOUT

# ============================================================



def logout():



    st.session_state.logged_in = False

    st.session_state.prediction = None



    st.rerun()





# END OF PART 2

# Continue by pasting Part 3 below this line.



# ============================================================

# PART 3: LOCATION SEARCH, DISTANCE AND ROUTE MAP

# ============================================================



# ------------------------------------------------------------

# GEOCODING: CONVERT A PLACE NAME INTO LATITUDE AND LONGITUDE

# ------------------------------------------------------------



@st.cache_data(ttl=3600, show_spinner=False)

def geocode_location(place):

    """

    Convert a location name or address into coordinates

    using OpenStreetMap Nominatim.

    """



    if not place or not place.strip():

        return None



    url = "https://nominatim.openstreetmap.org/search"



    params = {

        "q": place.strip(),

        "format": "jsonv2",

        "limit": 1,

    }



    headers = {

        "User-Agent": "TravelTimePredictionStudentProject/1.0"

    }



    try:

        response = requests.get(

            url,

            params=params,

            headers=headers,

            timeout=15,

        )



        response.raise_for_status()

        results = response.json()



        if not results:

            return None



        return {

            "latitude": float(results[0]["lat"]),

            "longitude": float(results[0]["lon"]),

            "display_name": results[0].get(

                "display_name", place

            ),

        }



    except (requests.RequestException, ValueError, KeyError):

        return None





# ------------------------------------------------------------

# HAVERSINE DISTANCE

# ------------------------------------------------------------



def haversine_distance(

    start_lat,

    start_lng,

    end_lat,

    end_lng,

):

    """

    Calculate straight-line distance between two coordinates

    in kilometres.

    """



    earth_radius_km = 6371.0



    lat1 = np.radians(start_lat)

    lat2 = np.radians(end_lat)



    delta_lat = np.radians(end_lat - start_lat)

    delta_lng = np.radians(end_lng - start_lng)



    a = (

        np.sin(delta_lat / 2) ** 2

        + np.cos(lat1)

        * np.cos(lat2)

        * np.sin(delta_lng / 2) ** 2

    )



    a = np.clip(a, 0.0, 1.0)



    central_angle = 2 * np.arcsin(np.sqrt(a))



    return float(earth_radius_km * central_angle)





# ------------------------------------------------------------

# GET ROAD ROUTE FROM OSRM

# ------------------------------------------------------------



@st.cache_data(ttl=1800, show_spinner=False)

def get_road_route(

    start_lat,

    start_lng,

    end_lat,

    end_lng,

):

    """

    Retrieve a road route from the public OSRM routing service.



    Returns road distance, road duration and route coordinates.

    """



    url = (

        "https://router.project-osrm.org/route/v1/driving/"

        f"{start_lng},{start_lat};{end_lng},{end_lat}"

    )



    params = {

        "overview": "full",

        "geometries": "geojson",

        "steps": "false",

    }



    try:

        response = requests.get(

            url,

            params=params,

            timeout=20,

        )



        response.raise_for_status()

        data = response.json()



        if (

            data.get("code") != "Ok"

            or not data.get("routes")

        ):

            return None



        route = data["routes"][0]



        coordinates = route["geometry"]["coordinates"]



        # OSRM coordinates are [longitude, latitude].

        route_points = [

            [latitude, longitude]

            for longitude, latitude in coordinates

        ]



        return {

            "distance_km": float(

                route["distance"] / 1000

            ),

            "duration_minutes": float(

                route["duration"] / 60

            ),

            "route_points": route_points,

        }



    except (

        requests.RequestException,

        ValueError,

        KeyError,

        IndexError,

    ):

        return None





# ------------------------------------------------------------

# CREATE INTERACTIVE FOLIUM MAP

# ------------------------------------------------------------



def create_route_map(
    start_lat,
    start_lng,
    end_lat,
    end_lng,
    pickup_name,
    drop_name,
    route_points=None,
):
    """Create an interactive map using standard OpenStreetMap tiles."""
    center_lat = (start_lat + end_lat) / 2
    center_lng = (start_lng + end_lng) / 2

    route_map = folium.Map(
        location=[center_lat, center_lng],
        zoom_start=12,
        control_scale=True,
        tiles=None,
    )

    folium.TileLayer(
        tiles="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        name="OpenStreetMap",
        overlay=False,
        control=True,
    ).add_to(route_map)

    folium.Marker(
        location=[start_lat, start_lng],
        tooltip="Pickup location",
        popup=folium.Popup(f"<b>Pickup</b><br>{pickup_name}", max_width=300),
        icon=folium.Icon(color="green", icon="play"),
    ).add_to(route_map)

    folium.Marker(
        location=[end_lat, end_lng],
        tooltip="Drop-off location",
        popup=folium.Popup(f"<b>Drop-off</b><br>{drop_name}", max_width=300),
        icon=folium.Icon(color="red", icon="flag"),
    ).add_to(route_map)

    if route_points and len(route_points) > 1:
        folium.PolyLine(
            locations=route_points,
            color="#A66BBE",
            weight=5,
            opacity=0.85,
            tooltip="Suggested road route",
        ).add_to(route_map)
    else:
        folium.PolyLine(
            locations=[[start_lat, start_lng], [end_lat, end_lng]],
            color="#A66BBE",
            weight=3,
            opacity=0.7,
            dash_array="8, 8",
            tooltip="Straight-line connection, not a road route",
        ).add_to(route_map)

    route_map.fit_bounds(
        [[start_lat, start_lng], [end_lat, end_lng]],
        padding=(35, 35),
    )
    return route_map


def google_maps_directions_url(

    pickup_name,

    drop_name,

):

    """

    Generate a Google Maps directions URL.

    No Google Maps API key is required for this link.

    """



    origin = quote(pickup_name, safe="")

    destination = quote(drop_name, safe="")



    return (

        "https://www.google.com/maps/dir/?api=1"

        f"&origin={origin}"

        f"&destination={destination}"

        "&travelmode=driving"

    )





# END OF PART 3

# Continue by pasting Part 4 below this line.



# ============================================================

# PART 4: RIDGE AND LASSO TRAVEL TIME PREDICTIONS

# ============================================================



def make_prediction(

    pickup,

    drop,

    departure_datetime,

):

    """

    Predict travel time using the saved Ridge and Lasso models.



    pickup and drop must contain:

        latitude, longitude, display_name

    """



    # --------------------------------------------------------

    # 1. Extract coordinates

    # --------------------------------------------------------



    start_lat = float(pickup["latitude"])

    start_lng = float(pickup["longitude"])



    end_lat = float(drop["latitude"])

    end_lng = float(drop["longitude"])



    # --------------------------------------------------------

    # 2. Calculate straight-line distance

    # --------------------------------------------------------



    straight_distance_km = haversine_distance(

        start_lat,

        start_lng,

        end_lat,

        end_lng,

    )



    # --------------------------------------------------------

    # 3. Extract date and time features

    # --------------------------------------------------------



    departure_datetime = pd.Timestamp(

        departure_datetime

    )



    hour = departure_datetime.hour

    day_of_week = departure_datetime.dayofweek

    month = departure_datetime.month

    is_weekend = int(day_of_week >= 5)



    # --------------------------------------------------------

    # 4. Prepare model input

    # --------------------------------------------------------



    feature_values = {

        "start_lng": start_lng,

        "start_lat": start_lat,

        "end_lng": end_lng,

        "end_lat": end_lat,

        "distance_km": straight_distance_km,

        "hour": hour,

        "day_of_week": day_of_week,

        "month": month,

        "is_weekend": is_weekend,

    }



    input_df = pd.DataFrame(

        [feature_values]

    )



    # Match the feature order used during training.

    input_df = input_df.reindex(

        columns=FEATURES,

        fill_value=0,

    )



    # --------------------------------------------------------

    # 5. Predict with Ridge and Lasso

    # --------------------------------------------------------



    ridge_model = bundle.get("ridge_model")

    lasso_model = bundle.get("lasso_model")



    if ridge_model is None or lasso_model is None:

        raise ValueError(

            "Ridge or Lasso model is missing from "

            "travel_time_models.pkl."

        )



    start_time = time.perf_counter()



    ridge_prediction = float(

        np.asarray(

            ridge_model.predict(input_df)

        ).reshape(-1)[0]

    )



    ridge_inference_ms = (

        time.perf_counter() - start_time

    ) * 1000



    start_time = time.perf_counter()



    lasso_prediction = float(

        np.asarray(

            lasso_model.predict(input_df)

        ).reshape(-1)[0]

    )



    lasso_inference_ms = (

        time.perf_counter() - start_time

    ) * 1000



    # Travel time cannot be negative.

    ridge_prediction = max(0.0, ridge_prediction)

    lasso_prediction = max(0.0, lasso_prediction)



    # --------------------------------------------------------

    # 6. Select the model with the lower validation MAE

    # --------------------------------------------------------



    if RIDGE_MAE <= LASSO_MAE:

        preferred_model = "Ridge Regression"

        preferred_prediction = ridge_prediction

        preferred_mae = RIDGE_MAE

    else:

        preferred_model = "Lasso Regression"

        preferred_prediction = lasso_prediction

        preferred_mae = LASSO_MAE



    # --------------------------------------------------------

    # 7. Obtain road distance and route duration

    # --------------------------------------------------------



    route = get_road_route(

        start_lat,

        start_lng,

        end_lat,

        end_lng,

    )



    if route:

        road_distance_km = route["distance_km"]

        osrm_duration_minutes = route["duration_minutes"]

        route_points = route["route_points"]

    else:

        road_distance_km = None

        osrm_duration_minutes = None

        route_points = None



    # --------------------------------------------------------

    # 8. Return results for the website

    # --------------------------------------------------------



    return {

        "pickup": pickup,

        "drop": drop,

        "departure_datetime": departure_datetime,

        "straight_distance_km": straight_distance_km,

        "road_distance_km": road_distance_km,

        "osrm_duration_minutes": osrm_duration_minutes,

        "route_points": route_points,

        "ridge_prediction": ridge_prediction,

        "lasso_prediction": lasso_prediction,

        "ridge_inference_ms": ridge_inference_ms,

        "lasso_inference_ms": lasso_inference_ms,

        "preferred_model": preferred_model,

        "preferred_prediction": preferred_prediction,

        "preferred_mae": preferred_mae,

    }





# END OF PART 4

# Continue by pasting Part 5 below this line.



# ============================================================

# PART 5: HOMEPAGE, ROUTE FORM, RESULTS AND APP EXECUTION

# ============================================================



def home_page():

    # --------------------------------------------------------

    # HEADER

    # --------------------------------------------------------



    header_left, header_right = st.columns([4, 1])



    with header_left:

        st.markdown(

            "\n".join(line.lstrip() for line in textwrap.dedent("""

            <div class="main-header">

                <div class="eyebrow">INTELLIGENT MOBILITY PLATFORM</div>

                <h1>Plan your journey.<br>Understand your travel time.</h1>

                <p>

                    Explore routes and compare predictions from

                    Ridge and Lasso Regression.

                </p>

            </div>

            """).splitlines()),

            unsafe_allow_html=True,

        )



    with header_right:

        st.write("")

        st.write("")

        st.button(

            "Log out",

            on_click=logout,

            use_container_width=True,

        )



    # --------------------------------------------------------

    # LOCATION INPUTS

    # --------------------------------------------------------



    st.markdown("## Plan your journey")

    st.caption(

        "Enter your pickup and destination, then select "

        "your planned departure date and time."

    )



    with st.container(border=True):



        country = st.selectbox(

            "Country",

            [

                "India",

                "United States",

                "United Kingdom",

                "Canada",

                "Australia",

                "Singapore",

                "United Arab Emirates",

            ],

            key="country",

        )



        col_pickup, col_swap, col_drop = st.columns(

            [5, 1, 5],

            vertical_alignment="bottom",

        )



        with col_pickup:

            pickup_text = st.text_input(

                "Pickup location",

                placeholder="e.g. Hyderabad Railway Station",

                key="pickup_location",

            )



        with col_swap:

            st.button(

                "⇄",

                key="swap_button",

                help="Swap pickup and destination",

                on_click=swap_locations,

                use_container_width=True,

            )



        with col_drop:

            drop_text = st.text_input(

                "Destination",

                placeholder="e.g. HITEC City, Hyderabad",

                key="drop_location",

            )



        date_col, time_col = st.columns(2)



        with date_col:

            departure_date = st.date_input(

                "Departure date",

                value=date.today(),

                key="departure_date",

            )



        with time_col:

            departure_hour = st.selectbox(

                "Departure hour",

                options=list(range(24)),

                index=9,

                format_func=lambda hour: (

                    f"{hour:02d}:00"

                ),

                key="departure_hour",

            )



        predict_clicked = st.button(

            "Calculate travel time",

            type="primary",

            use_container_width=True,

        )



    # --------------------------------------------------------

    # PROCESS THE REQUEST

    # --------------------------------------------------------



    if predict_clicked:



        if not pickup_text.strip() or not drop_text.strip():

            st.warning(

                "Please enter both pickup and destination."

            )

            return



        if pickup_text.strip().casefold() == drop_text.strip().casefold():

            st.warning(

                "Pickup and destination must be different."

            )

            return



        pickup_query = f"{pickup_text.strip()}, {country}"

        drop_query = f"{drop_text.strip()}, {country}"



        with st.spinner("Finding your locations..."):



            pickup = geocode_location(pickup_query)

            drop = geocode_location(drop_query)



        if pickup is None:

            st.error(

                "Could not find the pickup location. "

                "Try a more specific place name."

            )

            return



        if drop is None:

            st.error(

                "Could not find the destination. "

                "Try a more specific place name."

            )

            return



        if (

            pickup["latitude"] == drop["latitude"]

            and pickup["longitude"] == drop["longitude"]

        ):

            st.warning(

                "The selected locations have the same coordinates. "

                "Please choose different locations."

            )

            return



        departure_datetime = pd.Timestamp(

            year=departure_date.year,

            month=departure_date.month,

            day=departure_date.day,

            hour=int(departure_hour),

        )



        try:

            with st.spinner(

                "Calculating Ridge and Lasso predictions "

                "and retrieving the route..."

            ):

                result = make_prediction(

                    pickup,

                    drop,

                    departure_datetime,

                )



            st.session_state.prediction = result



        except Exception as error:

            st.error(

                "Unable to calculate the prediction. "

                "Please check the saved model and try again."

            )

            st.caption(f"Technical detail: {error}")

            return



    # --------------------------------------------------------

    # DISPLAY THE LATEST RESULT

    # --------------------------------------------------------



    result = st.session_state.get("prediction")



    if not result:

        st.markdown(

            "\n".join(line.lstrip() for line in textwrap.dedent("""

            <div class="empty-state">

                <div style="font-size: 42px;">✦</div>

                <h3>Your next journey starts here</h3>

                <p>

                    Enter two locations above to view the route,

                    compare model predictions and explore your

                    travel-time estimates.

                </p>

            </div>

            """).splitlines()),

            unsafe_allow_html=True,

        )

        return



    st.markdown("---")

    st.markdown("## Your journey insights")



    # --------------------------------------------------------

    # MAIN METRICS

    # --------------------------------------------------------



    metric1, metric2, metric3 = st.columns(3)



    with metric1:

        st.metric(

            "Ridge prediction",

            f'{result["ridge_prediction"]:.1f} min',

        )



    with metric2:

        st.metric(

            "Lasso prediction",

            f'{result["lasso_prediction"]:.1f} min',

        )



    with metric3:

        if result["road_distance_km"] is not None:

            st.metric(

                "Road distance",

                f'{result["road_distance_km"]:.2f} km',

            )

        else:

            st.metric(

                "Straight-line distance",

                f'{result["straight_distance_km"]:.2f} km',

            )



    # --------------------------------------------------------

    # RECOMMENDED MODEL

    # --------------------------------------------------------



    st.markdown(

        "\n".join(line.lstrip() for line in textwrap.dedent(f"""

        <div class="recommendation-card">

            <div class="eyebrow">MODEL WITH LOWER VALIDATION MAE</div>

            <h3>{result["preferred_model"]}</h3>

            <p>

                Estimated travel time:

                <strong>{result["preferred_prediction"]:.1f} minutes</strong>

            </p>

            <p>

                Validation MAE:

                <strong>{result["preferred_mae"]:.3f} minutes</strong>

            </p>

        </div>

        """).splitlines()),

        unsafe_allow_html=True,

    )



    # --------------------------------------------------------

    # ROUTE DETAILS

    # --------------------------------------------------------



    st.markdown("### Route details")



    detail1, detail2 = st.columns(2)



    with detail1:

        st.markdown("**Pickup**")

        st.write(result["pickup"]["display_name"])



    with detail2:

        st.markdown("**Destination**")

        st.write(result["drop"]["display_name"])



    st.write(

        "Departure:",

        result["departure_datetime"].strftime(

            "%d %B %Y at %H:%M"

        ),

    )



    if result["road_distance_km"] is not None:

        st.write(

            f'Road distance: {result["road_distance_km"]:.2f} km'

        )

        st.write(

            "OSRM route duration: "

            f'{result["osrm_duration_minutes"]:.1f} minutes'

        )

    else:

        st.info(

            "The road-routing service is unavailable right now. "

            "Showing the straight-line distance instead."

        )



    # --------------------------------------------------------

    # INTERACTIVE MAP

    # --------------------------------------------------------



    st.markdown("### Explore your route")



    route_map = create_route_map(

        result["pickup"]["latitude"],

        result["pickup"]["longitude"],

        result["drop"]["latitude"],

        result["drop"]["longitude"],

        result["pickup"]["display_name"],

        result["drop"]["display_name"],

        result.get("route_points"),

    )



    st_folium(

        route_map,

        width=None,

        height=520,

        returned_objects=[],

        key="journey_route_map",

    )



    # --------------------------------------------------------

    # GOOGLE MAPS LINK

    # --------------------------------------------------------



    maps_url = google_maps_directions_url(

        result["pickup"]["display_name"],

        result["drop"]["display_name"],

    )



    st.link_button(

        "Open directions in Google Maps ↗",

        maps_url,

        use_container_width=True,

    )



    # --------------------------------------------------------

    # MODEL COMPARISON

    # --------------------------------------------------------



    st.markdown("### Model comparison")



    comparison_df = pd.DataFrame(

        {

            "Model": [

                "Ridge Regression",

                "Lasso Regression",

            ],

            "Predicted time (minutes)": [

                result["ridge_prediction"],

                result["lasso_prediction"],

            ],

            "Inference time (ms)": [

                result["ridge_inference_ms"],

                result["lasso_inference_ms"],

            ],

            "Validation MAE (minutes)": [

                RIDGE_MAE,

                LASSO_MAE,

            ],

        }

    )



    st.dataframe(

        comparison_df.round(3),

        use_container_width=True,

        hide_index=True,

    )



    st.bar_chart(

        comparison_df.set_index("Model")[

            "Predicted time (minutes)"

        ]

    )



    # --------------------------------------------------------

    # IMPORTANT PROJECT LIMITATIONS

    # --------------------------------------------------------



    with st.expander("About these predictions"):



        st.write(

            "Ridge and Lasso predictions are generated from "

            "the historical data and the features used during "

            "model training."

        )



        st.write(

            "The road distance and route duration come from "

            "the external OSRM routing service. They are "

            "separate from the machine-learning predictions."

        )



        st.write(

            "These predictions do not use live traffic conditions. "

            "Accuracy may be limited for locations or travel "

            "patterns that differ from the training dataset."

        )



        st.write(

            "The validation MAE is a historical evaluation metric, "

            "not a guarantee of the error for this particular trip."

        )





# ============================================================

# APP EXECUTION

# ============================================================



if not st.session_state.logged_in:

    login_page()

else:

    home_page()





# END OF PART 5

# The app.py file is now complete.
