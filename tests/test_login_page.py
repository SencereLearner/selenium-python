import pytest
import allure

@allure.title("Check incorrect login error message")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('incorrect@test.com', 'incorrectPass')
    login_page.check_error_alert_text_is(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )

@allure.title("Check correct email with incorrect password error message")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_correct_email_with_incorrect_pass(login_page):
    login_page.open_page()
    login_page.fill_login_form('existint@email.com', 'non-existing-pass')
    login_page.check_error_alert_text_is(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )
