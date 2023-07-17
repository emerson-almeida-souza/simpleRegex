import re

class MatchsPattern:
    def __init__(self, text, pattern=""):
        self.pattern = pattern
        self.text = text

    def search_first_match_by_size(self, word_size: int, start_word="", end_word=""):
        pattern = f'{start_word}{("." * word_size)}{end_word}'
        re.compile(pattern)
        match = re.search(pattern, self.text)
        return match.group()

    def list_patterns_by_size(self, word_size: int, start_word="", end_word=""):
        pattern = f'{start_word}{("." * word_size)}{end_word}'
        re.compile(pattern)
        match = re.findall(pattern, self.text)
        return match

    def return_first_match(self):
        first_match = re.search(self.pattern, self.text)
        return first_match

    def pattern_equals_text(self):
        match = re.fullmatch(self.pattern, self.text)
        return match

    def list_match_pattern_text(self):
        match = re.findall(self.pattern, self.text)
        return match

    def different_from_pattern_to_text(self):
        difference = f"[^{self.pattern}]"  # Melhorar
        match = re.findall(difference, self.text)
        return match

    def start_with_the_pattern(self):
        pattern = f"^[{self.pattern}]"  # Melhorar
        match = re.findall(pattern, self.text)
        return match

    def match_cpf(self):
        pattern_cpf = re.compile(r"[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}")
        match = re.findall(pattern_cpf, self.text)
        return match

    def match_email(self):
        pattern_email = re.compile(r"[\w]*@[\w]*.com[.\w]*")
        match = re.findall(pattern_email, self.text)
        return match

    def match_cellphone(self):
        pattern_cellphone = re.compile(r"\(\d{2}\)\s\d\s[\d]{8}")
        match = re.findall(pattern_cellphone, self.text)
        return match


texto = """Emerson é lindo, Emerson é esbelto, meu cpf é 451.678.948.59, meu email é: em3rals@gmail.com.
Meu numero é: (19) 9 98278650"""
padrao = ""

matchs = MatchsPattern(texto)

print(matchs.match_cellphone())
