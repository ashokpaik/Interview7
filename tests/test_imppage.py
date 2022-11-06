import pytest

from testdata.testimppagedata import Testimppagedata
from testpageobjects.testimppageobjects import Testimppageobjects
from utilities.BaseClass import BaseClass


class Testimppage(BaseClass):

    @pytest.fixture(params=Testimppagedata.getTestData("Testcase1"))
    def getdata(self, request):
        return request.param

    def test_imppage(self, getdata):
        log = self.getLogger()
        log.info("Name is" + getdata["Firstname"])
        testimppageobject = Testimppageobjects(self.driver)
        testimppageobject.name().send_keys(getdata["Firstname"])
        testimppageobject.email().send_keys(getdata["Email"])
        testimppageobject.password().send_keys(getdata["Password"])
        testimppageobject.check().click()
        testimppageobject.select().send_keys("Female")
        testimppageobject.radio().click()
        testimppageobject.bday().send_keys(getdata["Birthday"])
        testimppageobject.btn().click()
        msg = testimppageobject.alert().text
        assert "Success" in msg
        self.driver.refresh()
