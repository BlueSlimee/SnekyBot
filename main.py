#                   SnekyBOT
#  O seu bot cobrinha preferido (powered by Python & Dreams)

from discord import Game
from os import listdir
from discord.ext import commands
import json

print("Carregando o Sneky...")
try:
    # Lendo as configurações do config.json
    with open('config.json') as configuracao:
        config = json.load(configuracao)
        # Antes de tudo, vamos confirmar que o usuário colocou o token do bot
        if config["token"] == "Insira o token aqui!":
            print("Oopsie Woopsie!\nVocê não colocou o token do seu bot na config.json...\nColoque o token lá e tente novamente. (Se você colocou, certifique-se de que você renomeou o arquivo para config.json, ao invés de config.json.example)!")
            exit(0)
except Exception as exe:
    # Se ele não encontrou o arquivo, retorna um erro
    print("Oopsie Woopsie!\nVocê esqueceu de colocar o config.json...\nColoque o config.json no mesmo diretorio do main.py.")
    exit(0)
     
# Vamos criar a variavel bot
bot = commands.Bot(command_prefix="s?", description="oi")
comandos = listdir('./comandos')

# Vamos carregar os eventos (que atualmente é só on_ready)
print("Carregando eventos...")
@bot.event
async def on_ready():
    print("Yay! O Sneaky está ligado.")
    await bot.change_presence(activity=Game(name="UNO com os membros do Vespertine Developers!"))

# Agora que temos o config.json certinho, vamos carregar os comandos.
if __name__ == "__main__":
    for cmd in comandos:
        # Se esse arquivo for realmente um arquivo Python, carregue ele.
        if cmd.endswith('.py'):
            print(f"Carregando o comando {cmd.split('.')[0]}")
            try:
                bot.load_extension(f'comandos.{cmd.split(".")[0]}')
                print(f"Comando {cmd.split('.')[0]} carregado!")
            except Exception as exce:
                print(f"Oopsie Woopsie, you made a fucky wucky!\nFalha no carregamento do comando {type(exce).__name__}!\n{exce}")
            
# Agora, vamos logar o bot.
bot.run(config["token"])