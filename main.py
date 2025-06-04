import streamlit as st
import read_data
from PIL import Image
import read_pandas
from datetime  import datetime



st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

# Legen Sie eine neue Liste mit den Personennamen an indem Sie ihre 
# Funktionen aufrufen
person_dict = read_data.load_person_data()
person_names = read_data.get_person_list(person_dict)
# bzw: wenn Sie nicht zwei separate Funktionen haben
# person_names = read_data.get_person_list()

# Nutzen Sie ihre neue Liste anstelle der hard-gecodeten Lösung
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")

# Dieses Mal speichern wir die Auswahl als Session State

st.write(f"Der Name ist: {st.session_state.current_user}") 


person_data = read_data.find_person_data_by_name(st.session_state.current_user)
picture_person = person_data["picture_path"]
geburtsjahr_person = person_data["date_of_birth"]
aktuelles_jahr = datetime.now().year
alter_person = aktuelles_jahr - geburtsjahr_person
max_HR_person = 220 - alter_person
st.write(f"Alter der Person: {alter_person} Jahre")
st.write(f"Maximale Herzfrequenz: {max_HR_person} bpm")
image = Image.open(picture_person)
st.image(image, caption=st.session_state.current_user)

df= read_pandas.read_my_csv()
df = read_pandas.add_heart_rate_zones(df, max_HR_person)

zone_durations = read_pandas.calculate_heart_rate_zones(df)

#zum ergebnisse anzeigen 
st.write("## Zeit in Herzfrequenzzonen")
for zone, duration in zone_durations.items():
    st.write(f"{zone}: {duration} Sekunden")

 #  Plot erstellen
fig = read_pandas.make_plot(df, max_HR_person)
st.plotly_chart(fig, use_container_width=True)   