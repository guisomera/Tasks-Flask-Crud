import flask
import requests

#CRUD
BASE_URL = 'http://127.0.0.1:5000'   #Defininando a URL q vai testar
tasks = []

def test_create_task():                                 #Criou função pra criar task tipo no postman
    new_task_data = { 
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa "      #Como se tivesse ido no post e mandando uma requisição (utilizando requests)
    }

    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)   #Response é  a resposta que o comando deu
    assert response.status_code == 200                                  #Se o status de  response for igual a 200, deu certo!!
    response_json = response.json()                                     #Pegando a resposta que foi passada em json no app
    assert "message" in response_json                                   #Verificando se tem mensagem no arquivo json
    assert "id" in response_json                                        #Verificiando se tem id
    tasks.append(response_json["id"])

def  test_get_tasks():  
     response = requests.get(f"{BASE_URL}/tasks")                       #Abre uma requisição no metodo get
     assert response.status_code == 200                                 #Confirma se deu certo (status 200)     
     response_json = response.json()                                    #Ele pega o corpo que é retornado quando pegamos as tarefa
     assert "tasks" in response_json                                    #Verifica se voltou a chave "tasks"
     assert "total_tasks" in response_json                              #Verifica se voltou a chave "Total_tasks" 

def test_get_task():
     task_id = 1
     if tasks:
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")          #Abre outra requisição no metodo get, porem com o parametro da task especifica
        assert response.status_code == 200                              #Verifica se o status é 200 (deu certo)
        response_json = response.json()                                 #Pega o que é retornado
        assert "id" in response_json                                    #Verifica se tem id 
        assert response_json['id'] == task_id                           #Verifica se o id é o mesmo solicitado

def test_update_task(): 
    if tasks:                                                            #Conferindo se tem task na  lista
        task_id = 1                                                       #Atribui a task que vou atualizar a 1 
        update = {                                                        #Novos atributos para a nova task
            'title': "titulo nova task",
            'description': "Descrição nova task",
            'completed': True
        }
                                                       
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update)         #Abrindo a requisição com metodo put pq ele vai pegar coisas dela 
        assert response.status_code == 200                                          #Conferindo se deu 200
        response_json = response.json()                                             #Pegando o que o corpo devolveu
        assert response_json.get('message') == "Tarefa atualizada com sucesso!!"    #Metodo get pega o que esta dentro de message, se o que esta dentro for igual a essa frase, deu certo

    #Nova requisão para a tarefa específica 
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")                  #Abrindo um get, para conseguir pegar as info da task
    assert response.status_code == 200                                                  #Conferindo se deu certo
    response_json = response.json()                                         #Pegando as info que o corpo retornou
    assert response_json['title'] == update['title']                        #Conferindo se o titulo esta igual ao nosso update (atualização)
    assert response_json['description'] == update['description']            #Testando descrição
    assert response_json['completed'] == update['completed']                #Testando se esta completa


       
        
