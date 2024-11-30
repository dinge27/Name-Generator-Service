from flask import Flask, request
import requests

app = Flask(__name__)

def request_names_from_API(gender, number):
    url = 'https://www.behindthename.com/api/random.json'
    api_key = "el280217681"
    response = requests.get(url, params={"gender": gender, "number": number, "key": api_key})

    if response.status_code == 200:
        list = response.json()
        return list
    else:
        print("Error:", response.status_code, response.text)

# Formats the list of names into a string
def format_name_list(name_list):
    list_string = ""
    for name in name_list["names"]:
        list_string = list_string + name + "\n"
    
    return list_string

@app.route('/name_generator', methods=['GET'])
def name_generator():
    gender = request.args.get("gender")
    number = request.args.get("number")

    name_list = request_names_from_API(gender, number)
    print(name_list)
    name_list_string = format_name_list(name_list)
    print(name_list_string)

    return name_list_string

if __name__ == "__main__":
    app.run(debug=True, port=5002)
    
    
