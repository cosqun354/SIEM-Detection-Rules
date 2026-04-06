import requests
import os
import glob
import urllib3

# Özü-imzalı (self-signed) sertifikat xətalarını gizlətmək üçün
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SPLUNK_URL = os.getenv('SPLUNK_URL')
SPLUNK_TOKEN = os.getenv('SPLUNK_TOKEN')

headers = {
    "Authorization": f"Bearer {SPLUNK_TOKEN}"
}

def deploy_rule(file_path):
    # Faylın adını qayda adı kimi götürürük (məs: detect_path_traversal)
    rule_name = os.path.basename(file_path).replace('.conf', '')
    
    with open(file_path, 'r') as f:
        splunk_query = f.read().strip()

    # Splunk Saved Search API Endpoint
    # "nobody" və "search" tətbiqi daxilində hamı üçün əlçatan edir
    api_url = f"{SPLUNK_URL}/servicesNS/nobody/search/saved/searches"
    
    # Qayda parametrləri
    payload = {
        "name": rule_name,
        "search": splunk_query,
        "is_scheduled": "1",
        "cron_schedule": "*/5 * * * *", # Hər 5 dəqiqədən bir işləsin
        "description": "GitHub Actions vasitəsilə avtomatik yüklənib.",
        "dispatch.earliest_time": "-1h",
        "dispatch.latest_time": "now"
    }

    # Öncə qaydanın mövcud olub-olmadığını yoxlayırıq (Update və ya Create üçün)
    check_url = f"{api_url}/{rule_name}"
    response = requests.get(check_url, headers=headers, verify=False)

    if response.status_code == 200:
        # Qayda artıq var, UPDATE edirik
        print(f"Yenilənir (Update): {rule_name}")
        requests.post(check_url, data={"search": splunk_query}, headers=headers, verify=False)
    else:
        # Qayda yoxdur, YENİSİNİ yaradırıq
        print(f"Yaradılır (Create): {rule_name}")
        requests.post(api_url, data=payload, headers=headers, verify=False)

# rules/splunk qovluğundakı bütün .conf fayllarını tap və göndər
conf_files = glob.glob("rules/splunk/*.conf")
for file in conf_files:
    deploy_rule(file)
