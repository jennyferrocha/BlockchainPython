# **BLOCKCHAIN EM PYTHON**

Este projeto implementa uma rede blockchain básica em Python. Ele permite a criação de transações entre endereços, a inclusão de blocos na rede, a mineração utilizando Proof of Work, a validação da blockchain e o histórico de transações por endereço.

A blockchain utiliza uma estrutura encadeada de blocos, onde cada bloco contém um conjunto de transações e um hash que o vincula ao bloco anterior. A mineração dos blocos é realizada com o algoritmo Proof of Work, garantindo a integridade e a segurança da rede.

## **Pré-requisitos**

Antes de executar o projeto, certifique-se de que os seguintes requisitos estejam instalados na sua máquina:

- [Visual Studio Code - VS CODE](https://code.visualstudio.com/Download)
- [Python 3.x](https://www.python.org/downloads/)
- Bibliotecas:
  - *datetime* 
  - *hashlib* 
  - *json*
- Um terminal ou console (como o Prompt de Comando no Windows, Terminal no macOS ou Linux)


## **Executando a aplicação**

Siga os passos abaixo para clonar o repositório e executar o projeto em sua máquina:

### **1. Clonar o repositório**

  - Deve-se clonar o repositório remoto para a sua máquina atual. Realize através do comando:

    ```bash
    git clone https://github.com/jennyferrocha/BlockchainPython.git
    ```

### **2. Navegar para o diretório do projeto**

  - Entre no diretório do projeto clonado:
  
    ``` bash
    cd BlockchainPython
    ```

### **3. Executar o código**
  - O código é executado diretamente no terminal ou no VS Code. Para isso, utilize o seguinte comando:

    ```bash
    python3 Blockchain.py
    ```

## **Funcionalidades**

### **1. Criar transações**
A blockchain começa com um bloco gênesis (o primeiro bloco da cadeia). A partir desse bloco, novos blocos são criados, cada um contendo transações pendentes e sendo vinculado ao bloco anterior através do seu hash.

### **2. Mineração dos blocos**

A mineração é realizada utilizando o algoritmo de Proof of Work. Para minerar um bloco, é necessário encontrar um nonce (número) tal que o hash do bloco comece com um número de zeros determinado pela dificuldade da rede.

#### Exemplo de mineração de bloco:
``` bash
bloco_anterior = blockchain.ultimo_bloco
prova_anterior = bloco_anterior.prova
nonce, hash_atual = blockchain.prova_de_trabalho(prova_anterior)
blockchain.criar_bloco(prova_anterior, nonce)

```

### **3. Criação de Transações**
O sistema permite a criação de transações entre endereços, onde um remetente envia um valor para um destinatário. As transações são adicionadas a um bloco que será minerado posteriormente.

#### Exemplo de criação de transação:

```bash
blockchain.criar_transacao("Jennyfer", "Gustavo", "R$300,00")
```

### **4. Histórico de Transações por Endereço**
A aplicação mantém o histórico de transações para cada endereço. É possível consultar o histórico de transações de um determinado endereço.

#### Exemplo de consulta ao histórico:
```bash
blockchain.exibir_historico_endereco("Jennyfer")
```

### **5. Validação da Blockchain**
A blockchain pode ser validada para garantir que todos os blocos da cadeia estão corretos. A validação verifica se os hashes dos blocos são consistentes e se a prova de trabalho foi realizada corretamente.

#### Exemplo de validação da blockchain:

```bash
blockchain.validar_cadeia()
```

### **Exemplo de Execução**
Ao executar o código, o console deve exibir as seguintes informações:

- Transações criadas.
- Mineração de novos blocos.
- Validação da blockchain.
- Exibição da blockchain com todos os blocos e transações.

#### Saída esperada no console:

```bash
Bloco gênesis criado: 1.
Transação criada: Jennyfer envia R$300,00 para Gustavo.
Transação criada: Gustavo envia R$60,00 para Maria.
Iniciando o Proof-of-Work...
Proof-of-Work concluído com sucesso: nonce=37560, hash=00004c7c6d3b2a9533688d516c4704a795f77d383a68015f6d7ecbfc1191b6bf

Iniciando o Proof-of-Work...
Proof-of-Work concluído com sucesso: nonce=37560, hash=00004c7c6d3b2a9533688d516c4704a795f77d383a68015f6d7ecbfc1191b6bf
Bloco 2 criado e adicionado à blockchain com hash 00004c7c6d3b2a9533688d516c4704a795f77d383a68015f6d7ecbfc1191b6bf.

Histórico de transações para Jennyfer:
{
    "Remetente": "Jennyfer",
    "Destinatario": "Gustavo",
    "Valor": "R$300,00"
}
```

## **Licença**

Este projeto está licenciado sob a licença [MIT](https://choosealicense.com/licenses/mit/).












  


