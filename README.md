# **BLOCKCHAIN EM PYTHON**

Este projeto implementa uma rede blockchain básica em Python. A aplicação permite a criação de transações, a inclusão de blocos na rede e a validação da cadeia. Esta blockchain simples utiliza Proof of Work para garantir a integridade dos blocos e das transações.

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
    python3 blockchain.py
    ```

## **Funcionalidades**

### **1. Criar transações**
O código cria transações entre usuários, onde um remetente envia um valor para um destinatário.

#### Exemplo de transação:

```
blockchain.criar_transacao("Jennyfer", "Gustavo", "R$300,00")
```

### **2. Mineração dos blocos**

Após criar transações, os blocos são minerados utilizando a técnica de Proof of Work. Isso garante a integridade da blockchain.

#### Exemplo de mineração de bloco:
``` bash
bloco_anterior = blockchain.obter_bloco_anterior()
prova_anterior = bloco_anterior['prova']
prova = blockchain.prova_de_trabalho(prova_anterior)
blockchain.criar_bloco(prova, blockchain.gerar_hash(bloco_anterior))
```

## **Exemplo de Execução**

Ao executar o projeto, o console deve exibir as seguintes informações:

- As transações criadas
- A mineração de novos blocos
- A validação da blockchain
- A exibição da blockchain completa com todos os blocos e transações

``` bash
Bloco 1 criado e adicionado à blockchain.
Transação criada: Jennyfer envia R$300,00 para Gustavo.
Transação criada: Gustavo envia R$60,00 para Maria.
Iniciando o Proof-of-Work...
Proof-of-Work concluído com sucesso: 53244.
Bloco 2 criado e adicionado à blockchain.
Iniciando a validação da blockchain...
A blockchain é válida.
```

## **Licença**

Este projeto está licenciado sob a licença [MIT](https://choosealicense.com/licenses/mit/).












  


