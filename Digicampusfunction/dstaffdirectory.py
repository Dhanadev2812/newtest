from telnetlib import EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Digicampushybrid.excelinputs import excel
import time
from DigicampusLocators.Dlocator import Dlocator
from excelinputs.excel import path
from excelinputs.excel import rowCount


class staff():

    def __init__(self, driver):
        self.driver = driver
        self.HR_sidemenu_linktext = Dlocator.HR_sidemenu_linktext
        self.Staffdirectory_sidemenu_linktext=Dlocator.Staffdirectory_sidemenu_linktext
        self.Addstaff_button_css_selector=Dlocator.Addstaff_button_css_selector

        self.employee_id_textbox_id = Dlocator.employee_id_textbox_id
        self.role_dropdown_name = Dlocator.role_dropdown_name
        self.name_textbox_id = Dlocator.name_textbox_id
        self.email_textbox_name = Dlocator.email_textbox_name
        self.gender_dropdown_name = Dlocator.gender_dropdown_name
        """self.dob_datepicker_name = Dlocator.dob_datepicker_name
self.submit_button_css_selector = Dlocator.submit_button_css_selector"""

    def staff_directory(self):
        HR = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.LINK_TEXT,Dlocator.HR_sidemenu_linktext)))
        action = ActionChains(self.driver)
        action.move_to_element(HR).perform()
        self.driver.implicitly_wait(7)
        Staff_directory = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT,Dlocator.Staffdirectory_sidemenu_linktext)))
        Staff_directory.click()

    def staff_add(self):
        self.driver.find_element(By.CSS_SELECTOR,Dlocator.Addstaff_button_css_selector).click()

    def staff_input(self):
        maxrow = rowCount(path,"Staff")
        for r in range(2,maxrow):
            print(r)
            employee_id = excel.readData(path, "Staff", r, 1)
            self.driver.find_element(By.ID,Dlocator.employee_id_textbox_id).click()
            self.driver.find_element(By.ID,Dlocator.employee_id_textbox_id).send_keys(employee_id)
            role = excel.readData(path, "Staff", r, 2)
            self.driver.find_element(By.NAME,Dlocator.role_dropdown_name).click()
            Select(self.driver.find_element(By.NAME,Dlocator.role_dropdown_name)).select_by_visible_text(role)
            name = excel.readData(path, "Staff", r, 3)
            self.driver.find_element(By.ID,Dlocator.name_textbox_id).send_keys(name)
            email = excel.readData(path, "Staff", r, 4)
            self.driver.find_element(By.NAME,Dlocator.email_textbox_name).send_keys(email)
            gender = excel.readData(path, "Staff", r, 5)
            self.driver.find_element(By.NAME, Dlocator.gender_dropdown_name).click()
            Gender = Select(self.driver.find_element(By.NAME, Dlocator.gender_dropdown_name))
            Gender.select_by_visible_text(gender)
            dob = excel.readData(path, "Staff", r, 6)
            self.driver.find_element(By.NAME, Dlocator.dob_datepicker_name).click()
            dob_string = dob.strftime("%m/%d/%Y")
            self.driver.find_element(By.NAME,Dlocator.dob_datepicker_name).send_keys(dob_string)
            time.sleep(3)
            self.driver.find_element(By.CSS_SELECTOR,"button[type='submit'][class='btn btn-info pull-right']").click()
            current_url = self.driver.current_url
            Expected_url = "http://localhost/projects/school_new3/admin/staff"
            if current_url == Expected_url:
                write = excel.writeData(path, "Staff", r, 7, "Staff added")
                return self.staff_add
            else:
                self.driver.get_screenshot_as_file(str(r) + "Staff_failed" + ".png")
                #Failure = excel.writeData(path, "Login", r, 4, "Invalid credentials")

    def staff_list(self):
        self.driver.get_screenshot_as_file("Staff_list" + ".png")





