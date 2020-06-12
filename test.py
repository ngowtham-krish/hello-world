import requests
import json

headers = {

    'Content-type': 'application/json'
    
}

data = {"catalog_key" : "value_of_catalog_key" , "project_key" : "value_of_project_key" }
str(data)
print(data)

# api to unpause the dag 
x =  requests.get("http://localhost:9020/api/experimental/dags/DAG3/paused/false")

#api to trigger as well to pass the params
response = requests.post('http://localhost:9020/api/experimental/dags/DAG3/dag_runs', headers=headers, json = {'conf': data})
print(response)



# headers = {
#     'Content-type': 'application/json'      
# }

# unpause = requests.get("http://strait-airflow:8080/api/experimental/dags/"+dag_id+"/paused/false")

# data = '{"catalog_key" : "value_of_catalog_key" , "project_key" : "value_of_project_key"}'
# url = 'http://strait-airflow:8080/api/experimental/dags/'+dag_id+'/dag_runs'
# trigger = requests.post(url, headers=headers, json = {'conf': data})
# response = "success"

