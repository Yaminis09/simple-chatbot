from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained("zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf")
def get_llm():
    
    return llm

# promptss = "what is the capital of India? give me one word answer"

# print(llm(promptss))
history = []
def get_prompt(instruction, history):
    # welcome_message = "Hello! how may I help you?"
    # prompt = f"Your question is :{instruction}\nAnswer:" 
    system = "You are an AI assistant that gives helpful answers. You answer the question in a short and concise way."
    # create prompt first
    prompt = f"### System:\n{system}\n\n"
    # add conversational histroy
    if history:
        prompt += f"{''.join(history)}"
    prompt = f"### User:\n{instruction}\n\n### Answer:\n"
    print(prompt)
    return prompt


# instruction = input("What is your question? ")
# prompt = get_prompt(instruction)

# llm.reset()
# for word in llm(prompt, stream=True):    
#     print(word, end="", flush=True)
# print()

# def ask_question():
#     prompt = get_prompt(instruction, history)
#     llm = get_llm()
#     llm.reset()
#     answer = ""
#     for word in llm(prompt, stream=True):    
#         print(word, end="", flush=True)
#         answer += word


#     pass

# while True:
#     instruction = input("What is your question? (To end the chat type 'bye') ")
#     # list of words to end the while loop
#     if instruction.lower() in ["end","bye","That's it", "Good bye", "exit"]:
#         break

#     prompt = get_prompt(instruction, history)
#     llm = get_llm()
#     llm.reset()
#     answer = ""
#     for word in llm(prompt, stream=True):    
#         print(word, end="", flush=True)
#         answer += word
#     print()
#     history.append(f"User: {instruction}")    
#     history.append(f"Assistant: {answer}") 

    

