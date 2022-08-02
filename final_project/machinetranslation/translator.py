import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


try:
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    language_translator.set_disable_ssl_verification(True)

    language_translator.set_default_headers(
        {'x-watson-learning-opt-out': "true"})

except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)


def englishToFrench(englishtext):
    if englishtext == "":
        englishtext = "Empty string"
    frenchtext = language_translator.translate(
        text=englishtext,
        model_id='en-fr').get_result()

    return frenchtext['translations'][0]['translation']


def frenchToEnglish(frenchtext):
    if frenchtext == "":
        frenchtext = "Chaîne vide"
    englishtext = language_translator.translate(
        text=frenchtext,
        model_id='fr-en').get_result()
    return englishtext['translations'][0]['translation']


#a = englishToFrench("Hello")
#b = frenchToEnglish("Bonjour")
