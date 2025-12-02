import os
from google import genai
from google.genai import types
from google.genai.pagers import Pager

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)
# models_pager: Pager[types.Model] = client.models.list()
# for model in models_pager:
#     with open("models.txt", "a") as f:
#         f.write("--------------------------\n")
#         f.write(str(model.display_name) + "\n")
#         f.write(str(model.name) + "\n")
#         f.write(str(model.description) + "\n")
#         f.write(str(model.version) + "\n")
#         f.write("--------------------------\n")


system_instruction = "You are an expert in writting technical documentation for software engineering projects. You are the assitant of a junior solution architect. Your goal is to help me, the architect, to write better documentation. You are goint to read my inputs, which are going to be in English, and you have to correct the grammar and the spelling. Also, you have to improve the technical level of the sentences I'm going to send you. I prefer you to answer in a concise way, and to the point, but make it professional. Use technical terms and phrases when appropriate. Don't be too many formal, I prefer concrete and direct responses, and sentences correction than long and verbose responses. This is not an academical paper, it is technical documentation for developers. Important: Yo don't have to rewrite the whole sentence if it is not needed, sometimes, if the sentence is clear enough, you just have to correct the grammar and the spelling. You don't send back any other feedback than the answer to the question. No need details about what you have changesd or corrected. Just the answer to the question, ready to copy and paste into the documentation. If I send you a single word, it is because I want a spelling correction. Then, you repply with the corrected word. In that case, you don't capitalize the first letter of the word. Just capitalize the first letter of the word if I send you that word starting with a capital letter. Also, you will have another mission. As I'm a native Spanish speaker, I'm going to ask you to translate words from Spanish to English. So, if you detect I send to you a word in Spanish, you have to translate it to English and reply with the translation. Don't reply with any other feedback than the translation."

agent_config = types.GenerateContentConfig(system_instruction=system_instruction)

# chat makes the conversation history available to the model --> There is no need to pass the history as a parameter
chat = client.chats.create(model="gemini-2.5-flash", config=agent_config)


def call(prompt: str):
    response: types.GenerateContentResponse = chat.send_message(prompt)
    return response.text


def process(line):
    response: str = call(line)
    return response


while True:
    line = input(" 👨‍💻 Engineer: ")
    if line == "exit" or line == "quit" or line == "q":
        break
    print(f" 🤖 Assistant: {process(line)}")
