from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
print("sample test case started")
driver = webdriver.Chrome()

excel_url = "https://docs.google.com/spreadsheets/d/18Zk3q_9_0wnjav7nSlLtnd6FW9CIgYS873kri-ctcRM/export?format=xlsx"
df = pd.read_excel(excel_url)

search_results = []

for keyword in df.iloc[:, 2]:
    driver.get('https://www.google.com')
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(keyword)
    time.sleep(2)

    suggestions = driver.find_elements(By.CSS_SELECTOR, '.sbct')
    longest_option = ""
    shortest_option = ""
    for suggestion in suggestions:
        text = suggestion.text
        if longest_option == "" or len(text) > len(longest_option):
            longest_option = text
        if shortest_option == "" or len(text) < len(shortest_option):
            shortest_option = text

    search_results.append({'Keyword': keyword, 'Longest Option': longest_option, 'Shortest Option': shortest_option})

driver.quit()

search_results_df = pd.DataFrame(search_results)

output_file_path = r'C:\Users\DCL\PycharmProjects\SeleniumTestPython\downloads\Search_Results.xlsx'
search_results_df.to_excel(output_file_path, index=False)

print(f"Search results saved to: {output_file_path}")
print("sample test case successfully completed")