import random
import string
from fastapi.testclient import TestClient

from bookmarkdto import BookmarkDto
from main import app

client = TestClient(app)


def test_a():
    assert 1 == 1