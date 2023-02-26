def calculate_bmi(client):
    height = client.height / 100
    bmi = client.weight / (height ** 2)
    return round(bmi, 2)


def calculate_bmr(client):
    if client.sex == 'M':
        bmi = 88.36 + (13.4 * client.weight) + (4.8 * client.height) - (5.7 * client.age)
    else:
        bmi = 447.6 + (9.2 * client.weight) + (3.1 * client.height) - (4.3 * client.age)
    return round(bmi, 2)
