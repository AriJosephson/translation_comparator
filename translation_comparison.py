# Main imports go here

# Import and set up Google Translate API.
from google.cloud import translate

project_id = "modular-seeker-345618"
assert project_id
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient.from_service_account_json("iaste.json")

def google_translate(text, target_language_code):
    response = client.translate_text(
    contents=[text],
    target_language_code=target_language_code,
    parent=parent)

    return response

# Import and set up txtai translation model.
from txtai.pipeline import Translation

# Create translation model
translate = Translation()

sample_text = "Hello world! This is a long text. Hopefully only one translation."
target_language_code = "fr"

language_list = ["ca","es","fr","ro"]

for language in language_list:
    for translation in google_translate(sample_text, language).translations:
        print(translation.translated_text)


languages = ["fr", "es", "de", "hi", "ja"]
translations = [translate("The sky is blue, the stars are far", language) for language in languages]
for i, text in enumerate(translations):
    print(f"Original Language: {languages[i]}")
    print(f"Translation: {text}")