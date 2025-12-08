import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_health():
    client = Client()
    resp = client.get(reverse("health"))
    assert resp.status_code == 200
    assert resp.json().get("status") == "ok"

@pytest.mark.django_db
def test_echo():
    client = Client()
    resp = client.post(reverse("echo"), data='{"x":1}', content_type="application/json")
    assert resp.status_code == 200
    assert resp.json().get("received", {}).get("x") == 1
