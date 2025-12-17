from ctransformers import AutoModelForCausalLM

# load model
llm = AutoModelForCausalLM.from_pretrained("zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf")
# call model
def get_llm():    
    return llm

history = []
def get_prompt(instruction, history):
    """
    Docstring for get_prompt
    
    :param instruction: Create prompt specific to give small and consise answers.
    :param history: List -> Stores the user chat history
    """   
    system = "You are an AI assistant that gives helpful answers. You answer the question in a short and concise way."
    # create prompt first
    prompt = f"### System:\n{system}\n\n"
    # add conversational histroy
    if history:
        prompt += f"{''.join(history)}"
    prompt = f"### User:\n{instruction}\n\n### Answer:\n"
    # print(prompt)
    return prompt

llm.reset()
def ask_question(instruction):
    """
    Docstring for ask_question
    
    :param instruction: calls LLM to yield word by word response and stream response to the UI
    Append instruction(question) and response to list history
    """
    global history
    prompt = get_prompt(instruction, history)
    llm = get_llm()
    llm.reset()
    answer = ""
    for word in llm(prompt, stream=True):    
        # print(word, end="", flush=True)
        answer += word
        # stream to UI
        yield word
    # Append instruction to list history
    history.append(f"User: {instruction}") 
    # Append llm response to    
    history.append(f"Assistant: {answer}") 
    






    

