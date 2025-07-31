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
    new_task = TaskManager(id= task_id_control, title=data.get("title"), description=data.get("description"))  #Data.get() pra pegar a info de dentro da chave tal, atribuindo aos elementos da minha classe
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso!!!"})

@app.route("/tasks", methods=['GET'])
def get_tasks   ():
    task_list = [task.to_dict() for task in tasks]              #Criamos outra lista pra dar saida, cada item em tasks vai ser adicionado em task_list pelo metodo to_dict()

    output = {                                      #Criou uma variavel de saida 
        "tasks": task_list,                         #Armazenou as listas 
        "total_tasks": len(task_list)
    }
    print(task_list)
    return jsonify(output)                          #Retornou a variável de saida em json

@app.route("/tasks/<int:id>", methods=['GET'])
def get_task(id):
    for t in tasks:                                 #Percorrendo a lista de atividade
        if t.id == id:                              #Pra ver se encontra o id q foi solicitado
            return jsonify(t.to_dict())             #Retornando essa atividade 
        
    return jsonify({"Message": "Não foi possível encontrar a atividade"}), 404

if __name__ == "__main__":      #Basicamente diz: "Se este arq  uivo esta sendo executado diretamente (e nao importado), rode o Flask"
    app.run(debug=True)         #Rodar o Flask e debug é utilizado para desenvolvedores