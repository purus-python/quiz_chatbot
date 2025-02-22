import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
FLASK_DEBUG = os.getenv("FLASK_DEBUG")
API_PORT = os.getenv('API_PORT')


AWS_REGION =os.getenv("AWS_REGION")
AWS_ACCESS_KEY_ID =os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")
ANTHROPIC_VERSION=os.getenv("ANTHROPIC_VERSION")
MODEL_ID=os.getenv("MODEL_ID")
SERVICE_NAME=os.getenv("SERVICE_NAME")
BUCKET_NAME = os.getenv("BUCKET_NAME")

PINECONE_API_KEY =os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME =os.getenv("PINECONE_INDEX_NAME")
PINECONE_REGION =os.getenv("PINECONE_REGION")
PINECONE_HOST =os.getenv("PINECONE_HOST")
PINECONE_NAME_SPACE =os.getenv("PINECONE_NAME_SPACE")

OPENAI_MODEL =os.getenv("OPENAI_MODEL")
OPENAI_API_KEY =os.getenv("OPENAI_API_KEY")
