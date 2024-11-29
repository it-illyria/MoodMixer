import os
from dotenv import load_dotenv
import secrets

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(32))
    DEVCYCLE_SDK_KEY = os.environ.get('DEVCYCLE_SDK_KEY', secrets.token_hex(32))
    DEBUG = True

