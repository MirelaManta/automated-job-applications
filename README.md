# LinkedIn Job Application Automation 

This is a Python script that uses Selenium WebDriver to automate the job application process on LinkedIn. It navigates to a job search page, signs in to your LinkedIn account, and applies to all the jobs that match your search criteria.
## Requirements
* Python 3.6 or higher
* ChromeDriver
* Selenium
* dotenv

## Installation
1. Install Selenium WebDriver and python-dotenv in your terminal by running:
```
pip install librabyname
```
2. Download ChromeDriver from the official website and place the executable file in a directory of your choice.
3. Update the __chrome_driver_path__ variable in the script to point to the location of the Chrome WebDriver executable on your computer.
## Usage
4. Set your LinkedIn email address, account password, and phone number as environment variables. Create a .env file in the same directory as the script, and add them like so:
```
    MY_EMAIL=your LinkedIn email address
    LNKD_PASSWORD=your LinkedIn password
    PHONE_NUM=your phone number
```
5. Update the URL variable in the script to match your job search criteria.
6. Run the script by typing python main.py in your terminal or command prompt.


## Notes
* The script starts by opening the Chrome browser and navigating to the LinkedIn job search page specified in the URL variable.
* It then clicks on the "Sign in" button, enters the user's email and password, and logs in to the LinkedIn account.
* A list of jobs is created from the search and each job is accessed in order. If an "Apply" button is available, it clicks on it and opens the application form. If the application form has a "Submit application" button, the script fills in the phone number field (if it is empty) and submits the application. If there is no "Submit application" button, it assumes that the application process has multiple steps and skips to the next job listing.
* The script closes any pop-ups(e.g discard application) or confirmation banners that appear after submitting the application.
