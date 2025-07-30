from flask import Flask, request, jsonify         #Importação do Flask, metodo request e para tambem retornar arquivos json
from models.task import TaskManager         #Da pasta models(pasta).task(nota), importa classe task
app = Flask(__name__)           #Atribuindo a classe flask em app, POO basico. __name__ é uma variavel especial que guarda o nome do arquivo atual

    # CRUD
    # Create, Read, Update and Delete
    # Tabela: Tarefa 

tasks = []
task_id_control = 1

@app.route("/tasks", methods=['POST'])          #Cria rota com /tasks. O 'Post'serve para ele receber info
def create_task():
    global task_id_control
    data = request.get_json()                   #Pega tudo que o usuário (Postman) escreveu e mandou, transformando em dicionário
    new_task = TaskManager(id= task_id_control, tittle=data.get("tittle"), description=data.get("description"))  #Data.get() pra pegar a info de dentro da chave tal, atribuindo aos elementos da minha classe
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso!!!"})


if __name__ == "__main__":      #Basicamente diz: "Se este arq  uivo esta sendo executado diretamente (e nao importado), rode o Flask"
    app.run(debug=True)         #Rodar o Flask e debug é utilizado para desenvolvedores