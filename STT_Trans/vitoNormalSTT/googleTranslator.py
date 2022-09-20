from googletrans import Translator

translator = Translator()

def GoogleTranslator(sentence):
    result = translator.translate(sentence, dest='en')
    return result.text

# print('나는 최고의 남자다. => ', GoogleTranslator('나는 최고의 남자다.'))