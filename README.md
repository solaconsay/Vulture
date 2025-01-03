# Vulture - Vulnerability Scanner
Vulture is a Python tool that checks the Common Vulnerabilities and Exposures (CVE) database for vulnerabilities in applications installed on your Windows machine.

## Features
  -  Automatic Application Detection: Identifies all installed applications on your system along with their version numbers.
  -  CVE Lookup: References each application against the CVE database to identify known vulnerabilities.
  -  Detailed Reporting: Displays the CVE ID, description, and a link for each detected vulnerability.

## Prerequisites
  -  Python 3.x
  -  nvdlib library (for CVE database access)
  -  winapps library (for accessing installed applications on Windows)

## Install required libraries with:
```cmd
  pip3 install nvdlib winapps
```

## Usage
1.  Run the script in your terminal:
```cmd   
  python vulture.py
```

3. This program will:
    -Gather all installed applications.
    -Search the CVE database for each application.
    -Display each vulnerability's ID, link, and description.
   
4.  The scanner pauses for 6 seconds between searches to manage API rate limits.

Code Overview
```python
  get_applications(): # Collects all installed applications and versions.
  get_cve_details(): # Searches the CVE database for each application.
  main(): # Runs the application scanner and processes the CVE information.
```
  
**Note**
Use Vulture responsibly, and ensure compliance with any applicable rate limits or usage policies for the CVE database.
