import flask
import requests

#CRUD
BASE_URL= 'http://127.0.0.1:5000'   #Defininando a URL q vai testar
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