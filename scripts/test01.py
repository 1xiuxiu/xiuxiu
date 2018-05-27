import allure
import pytest

class Test_001:
    @allure.step(title="测试步骤001")
    @pytest.mark.parametrize("a",[1,2,3])
    def test_abc(self, a):
        assert a!= 2


    @allure.step(title="测试步骤002")
    @pytest.mark.parametrize("a",[1,4,3])
    def test_bcd(self,a):
        allure.attach('描述','我是测试步骤002的描述')
        assert a !=2
