from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

driver = webdriver.Chrome()

driver.get("https://oibs2.metu.edu.tr/View_Program_Course_Details_64/main.php")
driver.implicitly_wait(7)
departmentCode = 178
departmentXpath = '//*[@id="single_content"]/form/table[2]/tbody/tr[1]/td[3]/select/option[' + str(departmentCode) + ']'
selectDepartment = driver.find_element_by_xpath(departmentXpath).click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="single_content"]/form/table[3]/tbody/tr/td/input').click() #submit button
rowSize = len(driver.find_elements_by_xpath('//*[@id="single_content"]/form/table[4]/tbody/tr')) # get row size (1,rowSize) (0 is not valid)

for i in range(2,rowSize+1): 
	rowString = '//*[@id="single_content"]/form/table[4]/tbody/tr[' + str(i) + ']/td[1]/font/input'
	driver.find_element_by_xpath(rowString).click()

	driver.find_element_by_xpath('//*[@id="single_content"]/form/table[2]/tbody/tr/td[1]/input').click()
	print(driver.find_element_by_xpath('//*[@id="single_content"]/form/table[1]/tbody/tr[2]/td[1]/font').text) # course code
	print(driver.find_element_by_xpath('//*[@id="single_content"]/form/table[1]/tbody/tr[2]/td[2]/font').text) # Course Name 
	print()
	sectionLength = len(driver.find_elements_by_xpath('//*[@id="single_content"]/form/table[3]/tbody/tr'))

	for k in range(4,sectionLength+1,2):
		countFixer = 0
		sectionNoString = '//*[@id="single_content"]/form/table[3]/tbody/tr[' + str(int(k)-1) + ']/td[1]/font/input'
		print("Section {}".format(driver.find_element_by_xpath(sectionNoString).get_attribute("value")))
		sectionTimeString = '//*[@id="single_content"]/form/table[3]/tbody/tr['+ str(k) + ']/td/table/tbody'
		if driver.find_element_by_xpath(sectionTimeString).text != "":
			print(driver.find_element_by_xpath(sectionTimeString).text)
		else:
			print("No Time")
		driver.find_element_by_xpath(sectionNoString).click()
		responseText = driver.find_element_by_xpath('//*[@id="formmessage"]/font/b').text
		if  responseText != "There is no section criteria to take the selected courses for this section.":
			givenDepartmentLength = len(driver.find_elements_by_xpath('//*[@id="single_content"]/form/table[3]/tbody/tr'))
			print("Departments: ",end="")
			for j in range(2,givenDepartmentLength+1):
				sectionString = '//*[@id="single_content"]/form/table[3]/tbody/tr[' + str(j) + ']/td[1]/font'
				print(driver.find_element_by_xpath(sectionString).text,end = " ")
			print()
			if k != sectionLength:
				print()
			driver.find_element_by_xpath('//*[@id="single_content"]/form/table[4]/tbody/tr/td/input').click()
		else:
			print("There is no section criteria to take the selected courses for this section.")
	print("--------------------------------------------------------------------------------------")
	driver.find_element_by_xpath('//*[@id="single_content"]/form/table[4]/tbody/tr/td/input').click()	



		
	
	
"""
23->business adm.
40-> ceng
50->econ
95-> history
107->ir
127 -> greek
157->philosophy
165->pol-sci
167 -> psy
178->soc
"""