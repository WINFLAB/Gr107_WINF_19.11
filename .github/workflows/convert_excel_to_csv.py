import pandas as pd
import requests
from io import BytesIO
excel_file_url = 'adres_url_pliku_excel_tutaj'
response = requests.get(excel_file_url)
excel_data = BytesIO(response.content)
df = pd.read_excel(excel_data)
df.to_csv('output.csv',index=False)
