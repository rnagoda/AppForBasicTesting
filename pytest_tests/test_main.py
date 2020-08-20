from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from string_values import StringValues as s
import random
from pytest import mark

desired_capabilities = {'automationName':'Appium',
                        'platformName':'Android',
                        'deviceName':'Android Emulator',
                        'app':'C:\\projects\\AndroidApps\\AppForBasicTesting\\apks\\app.apk'}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)


def assign_element(element_name):
    element_to_find = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, element_name)))
    return element_to_find


def get_element_text(element_name):
    element = assign_element(element_name)
    element_text = element.text
    return element_text


def convert_display_value(value):
    value = value[1:]
    value = value[:-2]
    value = int(value)
    return value


increment_button = assign_element(s.INCREMENT_BUTTON)
decrement_button = assign_element(s.DECREMENT_BUTTON)
reset_button = assign_element(s.RESET_BUTTON)
display_value_field = assign_element(s.DISPLAY_VALUE_TEXT_FIELD)

@mark.smoke
class TestButtonsExist:
    def test_increment_button_exists(self):
        assert assign_element(s.INCREMENT_BUTTON)

    def test_reset_button_exists(self):
        assert assign_element(s.RESET_BUTTON)

    def test_decrement_button_exists(self):
        assert assign_element(s.DECREMENT_BUTTON)


@mark.smoke
class TestTextFieldsExist:
    def test_header_field_exists(self):
        assert assign_element(s.HEADER_TEXT_FIELD)

    def test_display_value_field_exists(self):
        assert assign_element(s.DISPLAY_VALUE_TEXT_FIELD)


class TestButtonsWork:
    @mark.smoke
    def test_increment_button_increments(self):
        original_display_value = convert_display_value(display_value_field.text)

        increment_button.click()

        new_display_value = convert_display_value(display_value_field.text)

        if original_display_value < 10:
            assert new_display_value == original_display_value + 1
        else:
            assert new_display_value == original_display_value

    @mark.smoke
    def test_decrement_button_decrements(self):
        original_display_value = convert_display_value(display_value_field.text)

        decrement_button.click()

        new_display_value = convert_display_value(display_value_field.text)

        if original_display_value > 0:
            assert new_display_value == original_display_value - 1
        else:
            assert new_display_value == original_display_value

    def test_can_meet_random_display_value(self):
        original_display_value = convert_display_value(display_value_field.text)
        desired_display_value = random.randint(1,9)
        conversion_needed = desired_display_value - original_display_value

        if conversion_needed == 0:
            assert True
        else:
            if conversion_needed > 0:
                for i in range(0, conversion_needed):
                    increment_button.click()
            else:
                for i in range(conversion_needed, 0):
                    decrement_button.click()

            new_display_value = convert_display_value(display_value_field.text)

            assert new_display_value == desired_display_value

    @mark.smoke
    def test_reset_button_works(self):
        reset_button.click()
        display_value = convert_display_value(display_value_field.text)
        assert display_value == 0

    def test_maximum_increment_value(self):
        original_display_value = convert_display_value(display_value_field.text)

        if original_display_value == 10:
            decrement_button.click()

        while original_display_value < 10:
            increment_button.click()
            original_display_value = convert_display_value(display_value_field.text)

        increment_button.click()

        new_display_value = convert_display_value(display_value_field.text)

        assert new_display_value == 10
        

class TestWarningText:

    def test_maximum_increment_value_warning(self):

        original_display_value = convert_display_value(display_value_field.text)

        while original_display_value < 10:
            increment_button.click()
            original_display_value = convert_display_value(display_value_field.text)

        increment_button.click()
        increment_button.click()

        warning_text = get_element_text(s.WARNING_TEXT_FIELD)

        assert warning_text == s.WARNING_TEXT_MAX_VALUE

    def test_maximum_decrement_value_warning(self):

        original_display_value = convert_display_value(display_value_field.text)

        while original_display_value > 0:
            decrement_button.click()
            original_display_value = convert_display_value(display_value_field.text)

        decrement_button.click()
        decrement_button.click()

        warning_text = get_element_text(s.WARNING_TEXT_FIELD)

        assert warning_text == s.WARNING_TEXT_MIN_VALUE



