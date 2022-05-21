import aiogram.utils.markdown as fmt

def response_formation(data: dict) -> str:
    name = f"*{data['receipt_name']}*"
    ingridients = [f"{k} \- {v};" for k, v in data['ingridients'].items()]
    receipt = data['receipt']
    response = fmt.text(
        name + '\n',
        'Нам понадобится:',
        *ingridients,
        'Готовим:',
        receipt,
        sep='\n'
    )
    return response