import streamlit as st
from PIL import Image
from datetime import datetime

import read_data
import read_pandas
from person import Person

st.set_page_config(page_title="EKG Analyse", layout="wide")

st.title("EKG APP")

if 'current_user_name' not in st.session_state:
    st.session_state.current_user_name = 'None'

person_dict_list = read_data.load_person_data()
person_names = read_data.get_person_list(person_dict_list)

tab1, tab2 = st.tabs(["Personendaten", "EKG-Auswertung"])

with tab1:
    st.header("Versuchsperson auswählen")

    selected_name = st.selectbox(
        'Versuchsperson',
        options=person_names,
        index=person_names.index(st.session_state.current_user_name) if st.session_state.current_user_name in person_names else 0,
        key="sbVersuchsperson"
    )

    # Aktualisiere session state, wenn Auswahl geändert wurde
    if selected_name != st.session_state.current_user_name:
        st.session_state.current_user_name = selected_name
        # Lade Person neu
        person_data = read_data.find_person_data_by_name(selected_name)
        if person_data:
            st.session_state.current_person = Person(person_data)
        else:
            st.session_state.current_person = None

    st.write(f"Ausgewählt: {st.session_state.current_user_name}")

    if st.session_state.current_person is not None:
        person = st.session_state.current_person
        st.write(f"ID: {person.id}")   
        
    if 'current_person' in st.session_state and st.session_state.current_person is not None:
        person = st.session_state.current_person
        image = Image.open(person.picture_path)
        st.image(image, caption=st.session_state.current_user_name)

        alter = person.calculate_age()
        max_hr = person.calculate_max_heart_rate()

        st.write(f"Alter der Person: {alter} Jahre")
        st.write(f"Maximale Herzfrequenz: {max_hr} bpm")
    else:
        st.warning("Die gewählte Person konnte nicht gefunden werden.")

with tab2:
    st.header("EKG-Daten analysieren")

    if 'current_person' in st.session_state and st.session_state.current_person is not None:
        person = st.session_state.current_person
        max_hr = person.calculate_max_heart_rate()

        df = read_pandas.read_my_csv()
        df = read_pandas.add_heart_rate_zones(df, max_hr)

        fig = read_pandas.make_plot(df, max_hr)
        st.plotly_chart(fig, use_container_width=True)

        zone_durations = read_pandas.calculate_heart_rate_zones(df)
        avg_power_per_zone = read_pandas.calculate_average_power_per_zone(df)

        st.subheader("Durchschnittliche Leistung pro Herzfrequenzzone")
        st.write(avg_power_per_zone)

        st.subheader("Zeit in Herzfrequenzzonen")
        for zone, duration in zone_durations.items():
            st.write(f"{zone}: {duration} Minuten")
    else:
        st.info("Bitte zuerst eine Person im Tab 'Personendaten' auswählen.")

