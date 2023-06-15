from waitress import serve
from application.factory import create_app
from config import API_HOST,API_PORT

app = create_app()
if __name__ == '__main__':
    print('Starting mylocal_server on ',API_HOST,':',API_PORT)
    serve(app, 
          host= API_HOST,
          port = API_PORT,
          threads = 8)
    

# import os
# from dotenv import load_dotenv


# load_dotenv()
# x = os.getenv('CENSUS_URL_BASE')
# print(x)