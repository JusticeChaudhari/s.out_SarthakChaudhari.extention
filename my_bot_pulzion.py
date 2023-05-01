import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "I am your helper bot, please feel free to tell me anything that you have."}]
system_msg = "feel good bot" #yahape enter personal feel good bot 
messages.append({"role": "system", "content": system_msg})

#print("Your new assistant is ready!")
def feel_good_bot(user_input):
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    #print("\n" + reply + "\n")
    return reply


demo = gradio.Interface(fn=feel_good_bot, inputs = "text", outputs = "text", title = "Feel Good Bot")

demo.launch(share=True)