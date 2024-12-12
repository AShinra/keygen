import pickle
from pathlib import Path
import streamlit_authenticator as stauth


names = ['Jonathan Puray', 'Sheya Espaldon', 'Racquel Trillana', 'Andrea Joi Centeno', 'Ayessa Juraine Mancera', 'Ariza Alarcon', 'Paula Poblete', 'Mara Laya', 'Maria Anna Mae Paruan', 'Alvin Deocareza', 'Ayrone Masilungan', 'Christalline Llarena', 'Fritz Acebes']
usernames = ['athan', 'sheyaesp', 'kelly', 'axcnn', 'amancera', 'amalarcon', 'pau', 'mclaya', 'amaeparuan', 'adeocareza', 'vashy', 'talline', 'fritz']
passwords = ['adminako', '123mmi', 'mmi12345', '060895', 'ajmancera', 'amalarcon', 'mmitool', 'mara', '12345mmi', 'alvinmmi', 'stronger', 'tallinellarena082923', 'prets098']

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent/'hashed_pw.pkl'

with file_path.open('wb') as file:
    pickle.dump(hashed_passwords, file)