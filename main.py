import nvdlib
import winapps
import datetime
import time

def get_applications():
    app_name_version = {}
    for app in winapps.list_installed():
        if app.version is None:
            app_name_version[app.name] = ''
        else:
            app_name_version[app.name] = app.version
    return app_name_version
    

def get_cve_details(app_name,app_ver=None):
    print(f'Collecting information for {app_name} | Version: {app_ver}')
    cve_response = nvdlib.searchCVE_V2(keywordSearch=f'{app_name} {app_ver}',limit = None)    
    for each_cve in cve_response:
        print(each_cve.id)
        print(each_cve.url)
        print(each_cve.descriptions[0].value)


def main():
    # Get the application name and version dictionary
    app_name_version_dict = get_applications()
    # print(app_name_version_dict)
    
    # Iterate through the dictionary and call get_cve_details for each entry
    for app_name, app_ver in app_name_version_dict.items():
        get_cve_details(app_name, app_ver)
        time.sleep(6)


main()