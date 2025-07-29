from flask import Flask         #Importação normal

app = Flask(__name__)           #Atribuindo a classe flask em app, POO basico. __name__ é uma variavel especial que guarda o nome do arquivo atual

@app.route("/")                 #Atribuindo a rota, a string nos parenteses define o que vem depois do endereço (Netflix/conta)
def hello_word():               #Função normal de Hello word
    return "Hello word!"

@app.route("/about")            #Definindo outra rota, outra pagina
def about():                    
    return "Pag sobre"

if __name__ == "__main__":      #Basicamente diz: "Se este arq  uivo esta sendo executado diretamente (e nao importado), rode o Flask"
    app.run(debug=True)         #Rodar o Flask e debug é utilizado para desenvolvedores