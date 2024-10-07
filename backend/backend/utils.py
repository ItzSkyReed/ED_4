from datetime import datetime

import json


def write_to_data(json_data: dict):
    # Читаем существующие данные из файла
    with open('data.json', encoding='utf-8') as file:
        data: dict = json.load(file)

    json_data['date'] = int(datetime.strptime(json_data['date'], '%Y-%m-%d').timestamp())

    data[json_data.pop("model")] = json_data

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_model_data(model: str) -> None | dict:
    with open(r'data.json', encoding='utf-8') as file:
        data: dict = json.load(file)
    model_data = data.get(model)
    if model_data is not None:
        model_data["model"] = model
    return model_data

