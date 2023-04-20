from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
  "type": "service_account",
  "project_id": "hazel-lyceum-343617",
  "private_key_id": "4301bc65ab27a98744eecbe25c1130179bc2932a",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDY7F0vRoQZZDOy\nsh8vF+zhxWppVh8pcOlVQbTYioW/4H74rnUX06iimsutISyjU2WrVJiqw13/XeBb\nLFIxnVMCyHhOVN089Twqymybef+NH8iTveWDJuSMcXv3P4UvqcxI+uJXd+BxnZ7O\n+kgRcnL5KUaDn4a6YL3C6TCw1lkOQ5DMmSF2FJynuLGISglMfwzJPY3s0TZL1jyS\nK/YIPXQGCkw0By3IdCed6EaAnyL+k40k9EsZ5tA9chH9iAVewBtWMWd0+BMyS2z1\nWJTR7Hj/EIody5M5TDtbZyzOD6NbAR1oqgr+kEYCVvZIiCdejGHGJhmkgdEkhMK2\nSGPWupWpAgMBAAECggEADnQ6mCz5i85wTJIvjS4OXhzYRJyQdLXgMcGLo1Rp4ITh\ng0mlwXHTUsJkm1pbre968RVVZJSiSRCgSCnPS68H9YrxgmIZzhKW3pnpyZJWVgIb\nlaEr6wAiJeKugRMQK7BMu0JzMDVrgpRD1B/yVEBtKxPj24OpHoj6ibEdygYi5rFu\n8VNM2nJltX38CtMRzb6Rp3YN3yv0T8FaNPKn139UjxRhfaqqr3J2L2DpvWHc3t9K\nwwlY10jAThJu5NZxGdtVF9FdihtTcHTgXyz4g8eAQhbRfxoF+Z5geEszCb2ASpKi\n/b/77eQA0HSmkl0P262nailqLA0+2rhE8bDNelnXYQKBgQD7q52T1zzzz2zBRMtE\nSUq7eub9O4kQmaMUhREkamP11df9V8745acQhVPfQn4Fo9mHs9NTMAUTWktTr98S\nPco8ECzW6VeT8/PAyykv9aWVxKQSdM088UmgI0maVGKCH5ghOcW466C7msExRSiI\nSv0zF2nrj9OEZ4JlnQRNKTXmwwKBgQDcp7fswYY/ZXI9ECjf5eeBhrNhSVPeZMC+\nF72LaQlcHMdpm0Fug7JuBM0VzkyZMOBzDGQB2/yg0StX1sKp8wH+T1qcd/IcVV8P\njbL/HP8HpiTWUQUB2eDIp6dCUutz+HD3eHuBB8A/tVFJl+V8zARhvveN5xbY968a\nyiOkqb1DIwKBgD5xvX6CSFBiZiSqMhk2akGMZCXvELo6tLkRr0gu0bCcp6PnlqYx\nLTuvKTlbITO7DO1b1BJu9sNvgwM3vwyiojw28zk72owOWqu6fPS2aah4ixE9Q/Nc\nFx2Rw+B0EaEhv7h2wjV42X/TDR5xf3YZzStRIunc3OmcWUFnLTsL/6DLAoGAF8bi\n5No9sxslYjsZjHbjqWtwbO1P4kkNE+7O9/TLk2dufYzDUjtSwNQ3nT/rtR41MXCG\nXkTsRhAEEaUMuO98qYC3jODH8BGq+qwUO7VOLe7TTVzRo09tD3Ixbc4tnQOKeMA8\n3ryNFNBfAAUkL3x0hGvllR7vsVWPQt3BVX8M6+0CgYEA6RKDJ8mDVXO0ay6tTKMT\nKtPOYial2tAFgwdVhYs6X7cO/qu5GjGe9yMGAXkUhPS/wwmfdpqJm+06V94j4wIh\nbtLfvrZbXbIrZRbvHHNhbOX2ZPCrWZ1tlGNfCsbGna80w6rPRwdbbpNRnxB2a/Su\nKD05uLtChUl3++F14qZA+FU=\n-----END PRIVATE KEY-----\n",
  "client_email": "908573186440-compute@developer.gserviceaccount.com",
  "client_id": "110252518196254568444",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/908573186440-compute%40developer.gserviceaccount.com"
}

try:
    res = requests.get(
    f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

    print("loading...")

    soup = BeautifulSoup(res.text, 'html.parser')

    info = soup.find_all("span", class_ = "LrzXr kno-fv wHYlTd z8gr9e")[0].getText()

    print(info)

    credentials = service_account.Credentials.from_service_account_info(credentials_dict)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket('weather_py')
    blob = bucket.blob('weather_info.txt')

    ## with open('weather_info.txt', 'a') as f:
    ##    f.write(info + '\n')

    blob.upload_from_string(info + '\n')

    print('File uploaded.')

    print('Finished.')
except Exception as ex:
    print(ex)