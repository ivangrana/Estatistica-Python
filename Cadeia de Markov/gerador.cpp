//Algoritmo de geração de sequencias geneticas utilizando cadeias de Markov

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <cstdlib>
#include <ctime>

using namespace std;

// Nome do arquivo
const string arquivo = "sequencia.txt";

// Função responsavel por extrair a sequencia do arquivo
string Extrair() {
    ifstream fin(arquivo);
    string data, line;
    while (getline(fin, line)) {
        data += line;
    }
    fin.close();
    return data;
}

map<char, vector<char>> 

//função de criação do modelo de cadeia de markov
createModel(const string& data) 
{
    map<char, vector<char>> model;
    for (int i = 0; i < data.length() - 1; i++) {
        char current_char = data[i];
        char next_char = data[i+1];
        if (model.count(current_char) == 0) {
            model[current_char] = {next_char};
        } else {
            model[current_char].push_back(next_char);
        }
    }
    return model;
}

//Geração da nova sequência
string generateSequence(const map<char, vector<char>>& model, int new_sequence_length) {
    srand(time(NULL));
    string new_sequence;
    char current_char = model.begin()->first; // start with a random character
    new_sequence += current_char;
    for (int i = 0; i < new_sequence_length - 1; i++) {
        if (model.count(current_char) > 0) {
            vector<char> choices = model.at(current_char);
            int choice_index = rand() % choices.size();
            current_char = choices[choice_index];
        } else {
            current_char = model.begin()->first;
        }
        new_sequence += current_char;
    }
    return new_sequence;
}

// função main
int main() {
    
    string data = Extrair();
    
    map<char, vector<char>> model = createModel(data);
    
    
    int new_sequence_length = 61;
    string new_sequence = generateSequence(model, new_sequence_length);
    
    cout << new_sequence << endl;
    return 0;
}