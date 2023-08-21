import random

# Nome do arquivo
arquivo = "sequencia.txt"

# Função responsável por extrair a sequência do arquivo
def extrair():
    with open(arquivo, 'r') as fin:
        data = fin.read().replace('\n', '')
    return data

# Função de criação do modelo de cadeia de Markov
def create_model(data):
    model = {}
    for i in range(len(data) - 1):
        current_char = data[i]
        next_char = data[i + 1]
        if current_char not in model:
            model[current_char] = [next_char]
        else:
            model[current_char].append(next_char)
    return model

# Geração da nova sequência
def generate_sequence(model, new_sequence_length):
    random.seed()
    new_sequence = ""
    current_char = random.choice(list(model.keys()))  # comece com um caractere aleatório
    new_sequence += current_char
    for i in range(new_sequence_length - 1):
        if current_char in model:
            choices = model[current_char]
            choice = random.choice(choices)
            current_char = choice
        else:
            current_char = random.choice(list(model.keys()))
        new_sequence += current_char
    return str(new_sequence)

# Função main
def main():
    data = extrair()
    model = create_model(data)
    new_sequence_length = 12
    new_sequence = generate_sequence(model, new_sequence_length)
    print(new_sequence.upper())

if __name__ == "__main__":
    main()
