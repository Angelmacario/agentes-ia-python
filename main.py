from openai import OpenAI #classe base OpenAI
from dotenv import load_dotenv  # biblioteca do Python que vai carregar as informações do arquivo .env

load_dotenv()

cliente = OpenAI()

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Por que python é uma boa linguagem de programação?"
        }
    ],
    model="gpt-4o"
)

mensagem_resposta = resposta.choices[0].message 
conteudo_mensagem = mensagem_resposta.content 
role_mensagem = mensagem_resposta.role
print("Role: ", role_mensagem)
print("Content: ", conteudo_mensagem)

######## COMENTÁRIOS ########

# resposta = cliente.chat.completions.create( #estou configurando um chat e colocando um complemento para completar o chat
#     messages=[
#                   {"role": "user", "content": "Por que python é uma boa linguagem de programação"}] # [] lista de msgs com formato específico | {} dicionário role: quem está mandando essa msg e pra quem, e content que é o contéudo 
#     model="gpt-4o" #qual modelo quero usar
# )

# mensagem_resposta = resposta.choices[0].message #resposta da pergunta
# conteudo_mensagem = mensagem_resposta.content #pegar o conteudo
# role_mensagem = mensagem_resposta.role #quem mandou a msg
# print("Role: ", role_mensagem)
# print("Content: ", conteudo_mensagem)