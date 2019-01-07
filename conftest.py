import pytest

@pytest.fixture(scope='session')

def driver_get(request):
    from selenium import webdriver
    driver = webdriver.Chrome()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield
    driver.close()

