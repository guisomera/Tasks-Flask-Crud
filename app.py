from flask import Flask, request, jsonify   #Importação do Flask, metodo request e para tambem retornar arquivos json
from models.task import TaskManager         #Da pasta models(pasta).task(nota), importa classe task
app = Flask(__name__)                       #Atribuindo a classe flask em app, POO basico. __name__ é uma variavel especial que guarda o nome do arquivo atual

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
def get_tasks():
    task_list = [task.to_dict() for task in tasks]              #Criamos outra lista pra dar saida, cada item em tasks vai ser adicionado em task_list pelo metodo to_dict()

    output = {                                      #Criou uma variavel de saida 
        "tasks": task_list,                         #Armazenou as listas 
        "total_tasks": len(task_list)
    }
    print(task_list)
    return jsonify(output)                          #Retornou a variável de saida em json

@app.route("/tasks/<int:id>", methods=['GET'])      #Definimos parametro de rota(permite que voce recebe alguma variavel do usuario)
def get_task(id):
    for t in tasks:                                 #Percorrendo a lista de atividade
        if t.id == id:                              #Pra ver se encontra o id q foi solicitado
            return jsonify(t.to_dict())             #Retornando essa atividade 
        
    return jsonify({"Message": "Não foi possível encontrar a atividade"}), 404

@app.route("/tasks/<int:id>", methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:                                 #Procurei todos os itens em tasks e os chamei de t
        if t.id == id:                              #Se o id da task for igual o id que o usuario mandou 
            task = t                                #task é igual t 
    
    if task ==  None:                               #Se nao achar retorna essa mensagem 
        return jsonify({"message": "Não foi possível encontrar tarefa"}), 404
    
    data = request.get_json()                       #Mesma função q usei a cima pra pegar info que o usuario mandou no site 
    task.title = data['title']                      #Pegando e atribuindo novo titulo
    task.description = data['description']          #Pegando e atribuindo nova descrição
    task.completed = data['completed']              #Pegando e atribuindo se esta completa ou nao
   
    return jsonify({"message": "Tarefa atualizada com sucesso!!"}), 200

@app.route("/tasks/<int:id>", methods=['DELETE'])
def delete_tasks(id):
    global task_id_control 
    task = None
    for t in tasks:
        if t.id == id:
            task = t 
            task_id_control -= 1
            tasks.pop(id - 1)
            return jsonify({"message": "Tarefa deletada com sucesso!!"})
        
    if task == None:
        return jsonify({"message": "Não foi possível encontrar tarefa"})

if __name__ == "__main__":      #Basicamente diz: "Se este arq  uivo esta sendo executado diretamente (e nao importado), rode o Flask"
    app.run(debug=True)         #Rodar o Flask e debug é utilizado para desenvolvedores 