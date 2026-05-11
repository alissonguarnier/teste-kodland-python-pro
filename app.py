from flask import Flask, render_template
import random

# Inicializa a aplicação Flask
app = Flask(__name__)

# Listas de elementos para compor a ideia do jogo
temas = ["Zumbis", "Exploração Espacial", "Fantasia Medieval", "Cyberpunk", "Escola de Magia", "Fundo do Mar"]
mecanicas = ["Parkour", "Tycoon", "Sobrevivência", "RPG de Turnos", "Corrida de Obstáculos", "Puzzle"]
objetivos = [
    "Encontrar um tesouro lendário escondido", 
    "Escapar antes que o tempo acabe", 
    "Construir a maior base de todas", 
    "Derrotar o vilão que roubou as cores do mundo",
    "Resgatar os pets perdidos pelo mapa"
]

@app.route('/')
def pagina_inicial():
    # Utiliza a função integrada random.choice para selecionar itens aleatórios
    tema_escolhido = random.choice(temas)
    mecanica_escolhida = random.choice(mecanicas)
    objetivo_escolhido = random.choice(objetivos)
    
    # Renderiza o template HTML passando as variáveis geradas
    return render_template(
        'index.html', 
        tema=tema_escolhido, 
        mecanica=mecanica_escolhida, 
        objetivo=objetivo_escolhido
    )

if __name__ == '__main__':
    # Roda o servidor localmente no modo debug
    app.run(debug=True)