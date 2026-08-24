from collections import defaultdict
from translate import Translator


class TextAnalysis:

    memory = defaultdict(list)

    def __init__(self, text, owner):
        self.text = text
        self.owner = owner

        self.translation = self.__translate(
            self.text,
            "es",
            "en"
        )

        TextAnalysis.memory[self.owner].append(self)

        self.response = self.get_answer()

    def get_answer(self):
        res = self.__translate(
            "No sé cómo ayudar",
            "es",
            "en"
        )
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(
                from_lang=from_lang,
                to_lang=to_lang
            )

            translation = translator.translate(text)
            return translation

        except:
            return "Gagal menerjemahkan"
