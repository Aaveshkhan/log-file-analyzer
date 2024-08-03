# Log File Analyzer
Script that analyzes web server logs (e.g., Apache, Nginx) for common patterns such as the number of 404 errors, the most requested pages, or IP addresses with the most requests. Outputs a summarized report of all its findings on the console.

---

## Step 1: Install Python, PIP and VENV
`sudo apt install python3 python3-venv python3-pip`

## Step 2: Set up VENV directory
`python3 -m venv mytestenv`

## Step 3: Move files into VENV directory
`mv main.py requirements.txt mytestenv/`

## Step 4: Start up VENV
`cd mytestenv/`  <br />
`source ./bin/activate`

## Step 5: Install requirements.txt using pip
`python3 -m pip install -r requirements.txt`

## Step 6: Run the script
`python3 main.py`

---
