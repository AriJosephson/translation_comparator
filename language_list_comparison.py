# Comparing languages offered by Google Translate and txtai

google = """Afrikaans
Albanian
Amharic
Arabic
Armenian
Azerbaijani
Basque
Belarusian
Bengali
Bosnian
Bulgarian
Catalan
Cebuano
Chichewa
Chinese
Corsican
Croatian
Czech
Danish
Dutch
English
Esperanto
Estonian
Filipino
Finnish
French
Frisian
Galician
Georgian
German
Greek
Gujarati
Haitian
Hausa
Hawaiian
Hebrew
Hindi
Hmong
Hungarian
Icelandic
Igbo
Indonesian
Irish
Italian
Japanese
Javanese
Kannada
Kazakh
Khmer
Kinyarwanda
Korean
Kurdish (Kurmanji)
Kyrgyz
Lao
Latin
Latvian
Lithuanian
Luxembourgish
Macedonian
Malagasy
Malay
Malayalam
Maltese
Maori
Marathi
Mongolian
Burmese
Nepali
Norwegian
Oriya
Pashto
Persian
Polish
Portuguese
Punjabi
Romanian
Russian
Samoan
Scots Gaelic
Serbian
Sesotho
Shona
Sindhi
Sinhala
Slovak
Slovenian
Somali
Spanish
Sundanese
Swahili
Swedish
Tajik
Tamil
Tatar
Telugu
Thai
Turkish
Turkmen
Ukrainian
Urdu
Uyghur
Uzbek
Vietnamese
Welsh
Xhosa
Yiddish
Yoruba
Zulu"""

txtai = "Afrikaans (af), Amharic (am), Arabic (ar), Asturian (ast), Azerbaijani (az), Bashkir (ba), Belarusian (be), Bulgarian (bg), Bengali (bn), Breton (br), Bosnian (bs), Catalan; Valencian (ca), Cebuano (ceb), Czech (cs), Welsh (cy), Danish (da), German (de), Greek (el), English (en), Spanish (es), Estonian (et), Persian (fa), Fulah (ff), Finnish (fi), French (fr), Frisian (fy Western), Irish (ga), Scots Gaelic; Scottish Gaelic (gd), Galician (gl), Gujarati (gu), Hausa (ha), Hebrew (he), Hindi (hi), Croatian (hr), Haitian; Haitian Creole (ht), Hungarian (hu), Armenian (hy), Indonesian (id), Igbo (ig), Iloko (ilo), Icelandic (is), Italian (it), Japanese (ja), Javanese (jv), Georgian (ka), Kazakh (kk), Khmer (km Central), Kannada (kn), Korean (ko), Luxembourgish; Letzeburgesch (lb), Ganda (lg), Lingala (ln), Lao (lo), Lithuanian (lt), Latvian (lv), Malagasy (mg), Macedonian (mk), Malayalam (ml), Mongolian (mn), Marathi (mr), Malay (ms), Burmese (my), Nepali (ne), Dutch; Flemish (nl), Norwegian (no), Sesotho (ns Northern Sotho), Occitan (post 1500) (oc), Oriya (or), Punjabi; Panjabi (pa), Polish (pl), Pashto; Pushto (ps), Portuguese (pt), Romanian; Moldavian; Moldovan (ro), Russian (ru), Sindhi (sd), Sinhala; Sinhalese (si), Slovak (sk), Slovenian (sl), Somali (so), Albanian (sq), Serbian (sr), Swati (ss), Sundanese (su), Swedish (sv), Swahili (sw), Tamil (ta), Thai (th), Filipino (tl Tagalog), Tswana (tn), Turkish (tr), Ukrainian (uk), Urdu (ur), Uzbek (uz), Vietnamese (vi), Wolof (wo), Xhosa (xh), Yiddish (yi), Yoruba (yo), Chinese (zh), Zulu (zu)"

# print(google.split('\n'))
# print(txtai.split(', '))
# print(txtai.split(', ')[0][:-4])

google_list = google.split('\n')

txtai_list = []
split_txtai = txtai.split(', ')
for i in range(len(split_txtai)):
    if ';' in split_txtai[i]:
        txtai_list.append(split_txtai[i].split(';')[0])
    else:
        txtai_list.append(split_txtai[i].split(' ')[0])

# print(txtai_list)

only_google = [language for language in google_list if language not in txtai_list]
only_txtai = [language for language in txtai_list if language not in google_list]

print(only_google)
print(only_txtai)