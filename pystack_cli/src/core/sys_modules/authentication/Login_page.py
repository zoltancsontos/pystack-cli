from core.base_page import BasePage
from settings.settings import SETTINGS


class LoginPage(BasePage):
    """
    LoginPage logic
    """
    templates_dir = "templates/"
    template = SETTINGS['VIEWS']['DEFAULT_LOGIN_PAGE_TEMPLATE']

    def get_data(self, req):
        """
        Set up the data source
        Args:
            req: object
        Returns:
        """
        data = {
            "title": "PyStack Login",
            "text": "Please log in"
        }
        return data
