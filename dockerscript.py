from os import remove
import docker
from docker.api import container
client = docker.from_env()

#Printa todos os containers
def print_all_containers():
    container_list = client.containers.list()
    for container in container_list:
        print(f'Container ID: {container.id}')
        print(f'Container Short ID: {container.short_id}')
        print(f'Container Name: {container.name}')
        print(f'Container Status: {container.status}')
        
#Printa os containers que estão rodand
def get_containers_running():
    container_list = client.containers.list(filters={'status':'running'})
    if container_list:
        return container_list

#LISTA OS CONTAINERS E MOSTRA O SHORT_ID
def list_containers():
    containers_list = get_containers_running()
    if containers_list:
        for container in get_containers_running():
            print(container.short_id)

#REMOVE TODOS OS CONTAINERS
def remove_all_containers_running():
    containers_list = get_containers_running()
    if containers_list:
        for container in get_containers_running():
            try:
                print(f'Try remove container {container.name}')
                container.remove(force=True)
                print(f'Container callerd {container.name} removed sucessfully.')
            except Exception as err:
                pass
remove_all_containers_running()

#Starta ou stop os containers, no momento é necessário passar o ID do container, fazer um input pra poder escolher qual.
def action_container(containerid, action):
    if action.lower() in ['start','stop']:
        try:
            container = client.containers.get(containerid)
            try:
                result = getattr(container, action)
                print(f'Container call {container.name} {action}.')
            except Exception as err:
                print(f'Failed to start the container {container.name}')
        except docker.errors.NotFound:
            print('Container does not exist.')
    else:
        print('Invalid action.')

action_container('c3af53fde61e', 'stop')