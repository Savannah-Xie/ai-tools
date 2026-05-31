from tools.tools import *

TOOLS = {
  
    "update_essay": update_essay,
    "common_word_counter": common_word_counter,
    "sentence_counter": sentence_counter,
}

TOOL_DESCRIPTIONS = {
    "update_essay": "Updates text in the state with user given text that other tools will analyze. args: text: str",
    "common_word_counter": "Counts the common words in the texts. args: none",
    "sentence_counter": "Counts the sentences in the texts. args: none "
}