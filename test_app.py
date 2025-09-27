from app import app

def test_health():
    app.testing = True
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data == b'OK'
