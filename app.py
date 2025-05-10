
import streamlit as st

# -----------------------------
# CO2 Emission Factors (kg CO2)
# -----------------------------
CO2_CAR_KM = 0.192
CO2_FLIGHT = 250
CO2_DIET = {
    "Carnivore": 2500,
    "Vegetarian": 1700,
    "Vegan": 1500
}
CO2_KWH = 0.233

# -----------------------------
# App Layout
# -----------------------------
st.set_page_config(page_title="CO2 Footprint Calculator", layout="centered")
st.markdown("### 🌍")
st.title("Personal CO₂ Footprint Calculator")

st.markdown("Estimate your annual carbon footprint based on daily habits.")

# -----------------------------
# Inputs
# -----------------------------
st.header("Your Lifestyle Details")

km_per_week = st.slider("How many kilometers do you drive per week?", 0, 1000, 100)
flights_per_year = st.slider("How many flights do you take per year?", 0, 20, 2)
diet_type = st.selectbox("What is your diet type?", ["Carnivore", "Vegetarian", "Vegan"])
electricity_per_month = st.number_input("Monthly electricity usage (kWh)", 0.0, 2000.0, 300.0)

# -----------------------------
# CO2 Calculations
# -----------------------------
car_emission = km_per_week * 52 * CO2_CAR_KM
flight_emission = flights_per_year * CO2_FLIGHT
diet_emission = CO2_DIET[diet_type]
electricity_emission = electricity_per_month * 12 * CO2_KWH

total_emission = car_emission + flight_emission + diet_emission + electricity_emission

# -----------------------------
# Output Results
# -----------------------------
st.header("Your Estimated Annual CO₂ Emission")
st.success(f"🌱 **{total_emission:.2f} kg CO₂/year**")

st.markdown("#### Breakdown:")
st.write(f"🚗 Driving: `{car_emission:.2f}` kg CO₂")
st.write(f"✈️ Flights: `{flight_emission:.2f}` kg CO₂")
st.write(f"🥗 Diet: `{diet_emission:.2f}` kg CO₂")
st.write(f"⚡ Electricity: `{electricity_emission:.2f}` kg CO₂")

# -----------------------------
# Suggestions
# -----------------------------
st.header("Tips to Reduce Your Footprint")
st.markdown("""
- Carpool or use public transport when possible.
- Limit air travel and opt for trains.
- Shift towards a more plant-based diet.
- Save energy at home: LED bulbs, insulation, efficient appliances.
""")
