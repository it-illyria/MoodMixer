import os
from dotenv import load_dotenv
import secrets

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(32))
    DEVCYCLE_SDK_KEY = os.environ.get('DEVCYCLE_SDK_KEY', 'dvc_server_9107b48a_4c83_4012_a121_22a661e8a304_bff019f')
    DEBUG = True

