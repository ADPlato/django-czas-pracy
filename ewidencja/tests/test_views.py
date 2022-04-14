import pytest
from django.urls import reverse

from ewidencja.views import employees_view, managers_view, index_view, project_view, teams_view
from ewidencja.models import Employee

username = "user1"
password = "bar"

@pytest.mark.django_db
def test_employees_add(django_user_model):
    before = Employee.objects.all().count()
    user=django_user_model.objects.create_user(username=username, password=password)
    Employee.objects.create(first_name="Jan", last_name="Nowak", user=user)
    after = Employee.objects.all().count()
    assert after > before



