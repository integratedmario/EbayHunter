from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

import tkinter as tk
from tkinter import simpledialog

import csv

service = Service(r"C:\Users\kingm\Downloads\chromedriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.maximize_window()

try:
    #open ebay
    driver.get("https://www.ebay.com")
    
    #Find search bar and give it the search query
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    searchBar = driver.find_element(By.ID, "gh-ac")
    searchQuery = simpledialog.askstring("Input", "Input your eBay search query!")
    
    searchBar.send_keys(searchQuery)
    searchBar.send_keys(Keys.RETURN)
    
    time.sleep(1)
    
    sort_dropdown = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Sort")]')
    sort_dropdown.click()
    time.sleep(1)
    
    '''dropdown_items = driver.find_elements(By.XPATH, '//li')
    for item in dropdown_items:
        print(item.text)
        
    for item in dropdown_items:
        if "Price + Shipping: lowest first" in item.text:
            item.click()
            break'''
    
    '''WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//li[contains(text(), "Price + Shipping: Lowest first")]'))
    )'''
    
    sort_by_price = driver.find_element(By.XPATH, '//li/a[@sp="p2351460.m4116.l5869.c4"]')
    sort_by_price.click()

    time.sleep(3)
    
    product_data = []
    products = driver.find_elements(By.XPATH, '//div[contains(@class, "s-item__info")]')

    for product in products:
        try:
            title = product.find_element(By.XPATH, './/div[contains(@class, "s-item__title")]').text
            price = product.find_element(By.XPATH, './/span[contains(@class, "s-item__price")]').text
            link = product.find_element(By.XPATH, './/a[contains(@class, "s-item__link")]').get_attribute("href")
            product_data.append([title, price, link])
            print(f"{title} {price} {link}")
        except Exception as e:
            # Skip any items missing data
            print(f"Error extracting data for a product: {e}")
            continue
        
        # Save the data to a CSV file
    
    fileName = searchQuery.replace(" ","_").lower()
    
    '''with open(fileName + ".csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Title", "Price", "Link"])
        # Write the product rows
        writer.writerows(product_data)

    print("Data saved to " + fileName + ".csv.")'''

finally:
    print(0)

