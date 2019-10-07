from os import environ

from dotenv import load_dotenv

load_dotenv()


class Config:
    DISPLAY_PLOT = environ.get('DISPLAY_PLOT', 'true').lower() == 'true'
