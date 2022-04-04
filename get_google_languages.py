from os import environ

from google.cloud import translate

project_id = "modular-seeker-345618"
assert project_id
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient.from_service_account_json("C:/Users/Ari/Documents/Code/Python/flask/iaste.json")

response = client.get_supported_languages(parent=parent, display_language_code="en")
languages = response.languages

print(f" Languages: {len(languages)} ".center(60, "-"))
for language in languages:
    print(f"{language.language_code}\t{language.display_name}")




sample_text = "Hello world!"
target_language_code = "ar"

response = client.translate_text(
    contents=[sample_text],
    target_language_code=target_language_code,
    parent=parent,
)

for translation in response.translations:
    print(translation.translated_text)