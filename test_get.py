import pytest

@pytest.mark.usefixtures("driver_get")

class TestGet:
    def test_google(self):
        self.driver.get('https://google.com')
        assert self.driver.title == 'Google'
        
