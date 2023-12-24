import json
from string import punctuation


class PersianSwear:
    def __init__(self):
        with open(r"C:\Users\sh\Desktop\projects\Blogapi\blog\data.json", encoding='utf8') as file:
            self.data = json.load(file)
        self.swear_words = set(self.data["word"])

    def filter_words(self, text, symbol="*", ignoreOT=False):
        if not self.swear_words:
            return text
        if text is not None:
            words = text.split()
            filtered_words = []
            for word in words:
                if word in self.swear_words or (
                        ignoreOT and self.ignoreSY(word) in self.swear_words
                ):
                    filtered_words.append(symbol)
                else:
                    filtered_words.append(word)

            return " ".join(filtered_words)
        else:
            return text
