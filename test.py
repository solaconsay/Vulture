import nvdlib

app_name = 'Git'
app_ver = None

cve_response = nvdlib.searchCVE_V2(keywordSearch=f'{app_name} {app_ver}',limit = None)    
for each_cve in cve_response:
    print(each_cve.id)
    print(each_cve.url)
    print(each_cve.descriptions[0].value)
