import streamlit as st
from PIL import Image
from person import Person
from ekgdata import EKGdata

st.set_page_config(page_title="EKG Analyse", layout="wide")
st.title("EKG APP")

# Session-Variablen initialisieren
if 'current_user_name' not in st.session_state:
    st.session_state.current_user_name = 'None'
if 'current_person' not in st.session_state:
    st.session_state.current_person = None

# Daten laden
person_data_list = Person.load_person_data()
person_names = Person.get_person_list(person_data_list)

# Tabs
tab1, tab2 = st.tabs(["Personendaten", "EKG-Auswertung"])

# Tab 1 – Personendaten anzeigen
with tab1:
    st.header("Versuchsperson auswählen")

    selected_name = st.selectbox(
        "Versuchsperson",
        options=person_names,
        index=person_names.index(st.session_state.current_user_name) if st.session_state.current_user_name in person_names else 0,
        key="sbVersuchsperson"
    )

    if selected_name != st.session_state.current_user_name:
        st.session_state.current_user_name = selected_name
        person_dict = Person.find_person_data_by_name(selected_name)
        if person_dict:
            st.session_state.current_person = Person(person_dict)
        else:
            st.session_state.current_person = None

    st.write(f"Ausgewählt: {st.session_state.current_user_name}")

    if st.session_state.current_person is not None:
        person = st.session_state.current_person
        st.write(f"ID: {person.id}")

        image = Image.open(person.picture_path)
        st.image(image, caption=st.session_state.current_user_name)

        st.write(f"Alter der Person: {person.calculate_age()} Jahre")
        st.write(f"Maximale Herzfrequenz: {person.calculate_max_heart_rate()} bpm")
    else:
        st.warning("Die gewählte Person konnte nicht gefunden werden.")

# Tab 2 – EKG-Daten analysieren
with tab2:
    st.header("EKG-Daten analysieren")

    if st.session_state.current_person is not None:
        person = st.session_state.current_person
        ekg_tests = person.ekg_tests

        if ekg_tests:
            # Auswahlbox: verfügbare EKG-Test-IDs
            ekg_ids = [test["id"] for test in ekg_tests]
            selected_ekg_id = st.selectbox("Wähle EKG-Test-ID", ekg_ids)

            # Hole das passende EKG-Test-Dict
            selected_test = next((t for t in ekg_tests if t["id"] == selected_ekg_id), None)

            if selected_test:
                ekg = EKGdata(selected_test)
                ekg.find_peaks()
                hr = ekg.estimate_hr()

                st.write(f"Datum des Tests: {ekg.date}")
                st.write(f"Berechnete Herzfrequenz: {hr} bpm")
                st.plotly_chart(ekg.plot_time_series(), use_container_width=True)
            else:
                st.warning("Der ausgewählte EKG-Test konnte nicht geladen werden.")
        else:
            st.info("Für diese Person sind keine EKG-Tests vorhanden.")
    else:
        st.info("Bitte zuerst eine Person im Tab 'Personendaten' auswählen.")
