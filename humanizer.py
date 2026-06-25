"""
HumanizeAI Pro
Core Humanization Engine
"""

import re


class Humanizer:

    def __init__(self):
        self.version = "2.0"

    def clean_text(self, text):

        text = text.strip()

        text = re.sub(r"\s+", " ", text)

        return text

    def split_sentences(self, text):

        sentences = re.split(r'(?<=[.!?])\s+', text)

        return [s for s in sentences if s]

    def analyze(self, text):

        sentences = self.split_sentences(text)

        words = text.split()

        return {
            "characters": len(text),
            "words": len(words),
            "sentences": len(sentences),
            "paragraphs": len(
                [p for p in text.split("\n") if p.strip()]
            )
        }

    def humanize(self, text, style):

        text = self.clean_text(text)

        info = self.analyze(text)

        # AI Engine will be connected here later

        return text, info
