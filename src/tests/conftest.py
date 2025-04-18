import sys
import os

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)


def setup_test_environment():
    os.environ["TESTING"] = "true"

setup_test_environment()

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)