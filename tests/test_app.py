import pytest
import sys
sys.path.append("..")
from app import app as flask_app
from datetime import datetime

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    assert date in response.get_data(as_text=True)
    
def test_home_elements(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Bienvenido!" in response.get_data(as_text=True)
    assert '<img' in response.get_data(as_text=True)  # Verifica que la etiqueta <img> está presente

