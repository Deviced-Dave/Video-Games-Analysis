model = "gpt-3.5-turbo"

questions = [
    "Grand Theft Auto San Andreas",
]

conversation =[
    {"role": "system",
     "content":"You have to tell the year in which the games where published. You speak in a concise manner."},
    {"role":"user",
     "content":"Grand Theft Auto Vice city"},
    {"role":"assistant",
     "content":"2002"},
    ]

for question in questions:

    input_dict = {"role": "user",
                  "content": question}
    
    conversation.append(input_dict)  

    response = openai.ChatCompletion.create(
            model=model,
            messages=conversation,
            temperature=0.0,
            max_tokens=100
    )

    resp = response.choices[0]['message']['content']
    print(resp)

    resp_dict = {"role": "assistant",
                 "content": resp}
    
    conversation.append(resp_dict)