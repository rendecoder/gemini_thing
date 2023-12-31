import pathlib
import textwrap
import google.generativeai as genai

# Used to securely store your API key

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

keyshould = "o"
print("What is your API Key? Youcan get one at Google AI Studio ")
genai.configure(api_key=...)