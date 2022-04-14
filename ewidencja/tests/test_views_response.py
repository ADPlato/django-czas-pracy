import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_employees_response(client):
    response = client.get('/employees')
    assert response.status_code == 200


@pytest.mark.django_db
def test_employees_name_response(client):
    response = client.get(reverse('employee'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_employees_template(client):
    response = client.get('/employees')
    assert 'list_template.html' in (t.name for t in response.templates)

@pytest.mark.django_db
def test_managers_response(client):
    response = client.get('/managers')
    assert response.status_code == 200


@pytest.mark.django_db
def test_managers_name_response(client):
    response = client.get(reverse('manager'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_managers_template(client):
    response = client.get('/managers')
    assert 'list_template.html' in (t.name for t in response.templates)


@pytest.mark.django_db
def test_report_with_authenticated_client(client, django_user_model):
    username = "user1"
    password = "bar"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    response = client.get('/working-time')
    assert response.status_code == 200


@pytest.mark.django_db
def test_report_without_authenticated_client(client):
    response = client.get('/working-time')
    assert response.status_code != 200

@pytest.mark.django_db
def test_report_template(client, django_user_model):
    username = "user1"
    password = "bar"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    response = client.get('/working-time')
    assert 'work_time_form.html' in (t.name for t in response.templates)

@pytest.mark.django_db(transaction=False)
def test_index_response(client):
    response = client.get('/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_index_name_response(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_managers_template(client):
    response = client.get('/')
    assert 'index.html' in (t.name for t in response.templates)


@pytest.mark.django_db(transaction=False)
def test_project_response(client):
    response = client.get('/projects')
    assert response.status_code == 200

@pytest.mark.django_db
def test_project_name_response(client):
    response = client.get(reverse('project'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_projects_template(client):
    response = client.get('/projects')
    assert 'list_template.html' in (t.name for t in response.templates)


@pytest.mark.django_db(transaction=False)
def test_team_response(client):
    response = client.get('/teams')
    assert response.status_code == 200

@pytest.mark.django_db
def test_team_name_response(client):
    response = client.get(reverse('team'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_team_template(client):
    response = client.get('/teams')
    assert 'list_template.html' in (t.name for t in response.templates)
