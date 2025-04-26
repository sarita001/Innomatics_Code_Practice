<!DOCTYPE html>
<html>
<head><title>RegW Webpage Simulation</title></head>
<body>
<h2>RegW Transaction Search</h2>

<form id="searchForm">
    Transaction ID: <input type="text" id="txn_id"><br><br>
    Start Date: <input type="date" id="start_date"><br><br>
    End Date: <input type="date" id="end_date"><br><br>
    <button type="button" onclick="showResult()">Search</button>
</form>

<div id="result" style="display:none;">
    <h3>Transaction Found!</h3>
    <p>Report Date: <span id="report_date">2025-04-25</span></p>
    <p>Amount: <span id="amount">1000</span></p>
    <p>Header: <span id="header">Report_A</span></p>
    <button onclick="viewAttachment()">View Attachment</button>
</div>

<script>
function showResult() {
    document.getElementById('result').style.display = 'block';
}
function viewAttachment() {
    alert('Viewing Attachment: Report Date=2025-04-25, Amount=1000, Header=Report_A');
}
</script>
</body>
</html>






import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui

# Setup
input_excel = 'input/transactions.xlsx'
regw_html = 'input/regw_page.html'
screenshot_folder = 'output/screenshots'
summary_report = 'output/summary_report.xlsx'
email_draft = 'output/email_draft.txt'

os.makedirs(screenshot_folder, exist_ok=True)

# Read transactions
df = pd.read_excel(input_excel)

# Create Browser
options = Options()
options.add_experimental_option("detach", True)  # keeps browser open
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()

# Open local RegW page
driver.get('file://' + os.path.abspath(regw_html))
time.sleep(2)

summary_data = []

# Process each transaction
for idx, row in df.iterrows():
    txn_id = row['Transaction_ID']
    expected_date = str(row['Expected_Report_Date']).split()[0]
    expected_amount = str(row['Expected_Amount'])
    expected_header = row['Expected_Header']

    # Fill Form
    driver.find_element(By.ID, 'txn_id').clear()
    driver.find_element(By.ID, 'txn_id').send_keys(txn_id)
    driver.find_element(By.ID, 'start_date').send_keys('2025-04-01')
    driver.find_element(By.ID, 'end_date').send_keys('2025-04-30')
    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    time.sleep(2)

    # Screenshot
    screenshot_path = os.path.join(screenshot_folder, f'{txn_id}.png')
    pyautogui.screenshot(screenshot_path)
    print(f"Screenshot saved for {txn_id}")

    # Read results
    actual_date = driver.find_element(By.ID, 'report_date').text
    actual_amount = driver.find_element(By.ID, 'amount').text
    actual_header = driver.find_element(By.ID, 'header').text

    # Reconciliation
    match_status = "Match"
    if (expected_date != actual_date) or (expected_amount != actual_amount) or (expected_header != actual_header):
        match_status = "Mismatch"

    # Store
    summary_data.append({
        'Transaction_ID': txn_id,
        'Expected_Report_Date': expected_date,
        'Actual_Report_Date': actual_date,
        'Expected_Amount': expected_amount,
        'Actual_Amount': actual_amount,
        'Expected_Header': expected_header,
        'Actual_Header': actual_header,
        'Status': match_status,
        'Screenshot_Path': screenshot_path
    })

    time.sleep(2)  # small wait

# Create Summary Excel
summary_df = pd.DataFrame(summary_data)
summary_df.to_excel(summary_report, index=False)
print(f"Summary Report created: {summary_report}")

# Mock Email
with open(email_draft, 'w') as f:
    f.write("Subject: RegW Report Reconciliation Summary\n\n")
    f.write("Hi Team,\n\n")
    f.write("Please find below the summary of reconciliation.\n\n")
    f.write(summary_df.to_string(index=False))
    f.write("\n\nScreenshots are stored at: output/screenshots/\n")
    f.write("\nThanks,\nAutomation Bot")

print(f"Email draft created: {email_draft}")

driver.quit()







# Open RegW actual URL
driver.get('https://your-regw-website.com')
time.sleep(2)

# Find username and password fields, enter credentials
driver.find_element(By.ID, 'username').send_keys('your_username')
driver.find_element(By.ID, 'password').send_keys('your_password')

# Click login
driver.find_element(By.ID, 'loginButton').click()
time.sleep(3)





# Click View Attachment button
driver.find_element(By.ID, 'viewAttachmentButton').click()

# Switch to new window
driver.switch_to.window(driver.window_handles[1])

# Now read attachment fields

# Close attachment window after reading
driver.close()

# Switch back to main window
driver.switch_to.window(driver.window_handles[0])




import pdfplumber

with pdfplumber.open('downloaded_file.pdf') as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
    print(text)



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "your_email@domain.com"
receiver = "team_email@domain.com"
password = "your_email_password"

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = "RegW Summary Report"
body = "Please find attached report."

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()
