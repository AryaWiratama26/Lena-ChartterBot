from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Lena")

trainer = ListTrainer(chatbot)
with open("data_train.txt", "r", encoding="utf-8") as file:
    conversation = file.read().split("\n")
    
trainer.train(conversation)

exit_conditions = [":q", "quit", "exit"]
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"Lena : {chatbot.get_response(query)}")