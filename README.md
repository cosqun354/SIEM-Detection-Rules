# Splunk Detection Rules (Detection as Code)

Bu repozitoriya **Splunk SIEM** sistemi üçün nəzərdə tutulmuş professional aşkarlama qaydalarını (detection rules) ehtiva edir. Layihə müasir SOC mühitlərində tətbiq olunan "Detection as Code" prinsipləri əsasında qurulmuşdur.

## Layihənin Məqsədi
Aşkarlama qaydalarının birbaşa SIEM interfeysində deyil, mərkəzləşdirilmiş GitHub mühitində idarə olunmasını, versiya nəzarətini və API vasitəsilə SIEM-ə avtomatik inteqrasiyasını təmin etməkdir.

## Repozitoriyanın Strukturu
* `/rules/splunk`: Splunk üçün SPL (Search Processing Language) formatında hazırlanmış professional qaydalar.
* `/scripts`: Qaydaların GitHub-dan Splunk API-nə sinxronizasiyası üçün nəzərdə tutulmuş avtomatlaşdırma skriptləri.

## İstifadə Olunan Texnologiyalar
* **SIEM:** Splunk
* **Version Control:** GitHub
* **Automation:** Python (Splunk SDK / REST API)
* **Log Source:** Docker JSON logs
