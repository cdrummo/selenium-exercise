# Fetch Coding Exercise - SDET

## 📖      Project Information & Author:

Name              | Username(GitHub)
----------------- |------------------
Connor Drummond   | cdrummo

### ⭐ Project Requirements:
1. Play around with the website and find the best algorithm (minimum number of weighings for any possible
fake bar position) to find the fake gold bar.
2. Create the test automation project using any preferred language to perform
   * Clicks on buttons (“Weigh”, “Reset”)
   * Getting the measurement results (field between the 'bowls')
   * Filling out the bowls grids with bar numbers (0 to 8)
   * Getting a list of weighing
   * Clicking on the gold bar number at the bottom of the website and checking for the alert message
3. Code the algorithm from step 1 which uses a set of actions from step 2 to find the fake gold bar
The algorithm should populate and weigh gold bars until a fake one is found, click on a fake bar number, output the
alert message, number of weighing, and list of weighing made

## ⚙️ Quick Start:

### Dependencies:

Dependency    | Version      
------------  | -------------
Python        | 3.12.4       
Selenium      | 4.23.1       
Webdriver     | 4.0.2        
Google Chrome | 127.0.6533.89

⚠️**NOTE:** Package versions may be important to running the code.

### 1. Installing Python:

⚠️**NOTE:** These steps assume you are using Microsoft Windows device. If you are using different Operating system please install using appropriate package manager.

From the Windows command line, run the following command(may need to run as asministrator):

    winget install python3

### 2. Installing Selenium:

⚠️**NOTE:** If pip/python commands are not running on the command line it is possible it is not in the system path or changes to system path have not been activated. In most cases restarting your computer will apply system path variables and allow you to proceed.

From the Windows command line, run the following command:

    pip install selenium

### 3. Installing Webdriver:

From the Windows command line, run the following command:

    pip install selenium

### 4. Installing Google Chrome:

From the Windows command line, run the following command:

    winget install Google.Chrome

## 🏃‍ Running the Application:

After installing all the necessary packages from the Dependencies section above, use the command line to navigate to the python file location:

     cd <FILE_PATH>

From this point it run the python/selenium script using the following command:

    python selenium-excercise.py

## 💭 The solution and thoughts behind code:

![alt text](https://github.com/cdrummo/selenium-exercise/blob/9865b765d700900066f69c66508070dabc8a92a0/Org%20charts.jpeg)

The above image shows the decision flow for the algorithm I used. The reason for the algorithm I chose was that it will always get the right answer in two steps.

The basic idea is to narrow down the choices from nine bars to three bars. From here we can easily determine which bar is fake by comparing two of the remaining three bars.


## Implementation:

In the first section of the code I am importer the necessary selenium packages and webdriver packages to use in the code. After importing, I setup the variables and options in order to launch the Google Chrome browser for the automation. I added the experimental option to "detach" to the options as I wanted the Browser to remain open after the code finsihes so that the user can see what happened in script. After launching the browser, I load the website in which the script will run.

```python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("http://sdetchallenge.fetch.com/")


```
