import streamlit as st
import read_data
from PIL import Image

st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Session State wird leer angelegt, solange er noch nicht existiert
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

# Laden eines Bilds
image = Image.open("data/pictures/js.jpg") #Jannic
# Anzeigen eines Bilds mit Caption
st.image(image, caption=st.session_state.current_user) 

image = Image.open("data/pictures/tb.jpg") #Julian
# Anzeigen eines Bilds mit Caption
st.image(image, caption=st.session_state.current_user)

image = Image.open("data/pictures/bl.jpg") #Yunus
# Anzeigen eines Bilds mit Caption
st.image(image, caption=st.session_state.current_user)

