# **SIMULAÇÃO DE BLOCKCHAIN EM PYTHON**

Este projeto implementa uma rede blockchain simplificada em Python. Ele demonstra conceitos fundamentais como blocos, transações, proof-of-work, gerenciamento de saldos, taxas de transação e resolução de forks.

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

- **Criação de Blocos:** Gera novos blocos contendo transações e os adiciona à cadeia.
- **Transações:** Permite a criação de transações entre diferentes endereços, incluindo taxas.
- **Proof-of-Work (PoW):** Utiliza um algoritmo PoW simplificado para simular a mineração de blocos.
- **Gerenciamento de Saldos:**  Rastreia os saldos de cada endereço e garante que as transações sejam válidas.
- **Taxas de Transação:**  Inclui taxas nas transações, que são recompensadas aos mineradores.
- **Resolução de Forks:** Implementa uma lógica simples para resolver forks, selecionando a cadeia mais longa.
- **Propagação de Blocos e Transações:** Simula a propagação de informações pela rede.

## **Limitações**

Este projeto é uma simulação simplificada e **não se destina ao uso em produção**.  Ele não inclui recursos importantes de uma blockchain real, como:

- **Segurança robusta:** Assinaturas digitais, criptografia avançada, etc.
- **Persistência de Dados:** Armazenamento em banco de dados ou arquivo.
- **Rede P2P completa:**  Comunicação real entre nós.
- **Mecanismo de Consenso Robusto:** Implementação completa de PoW, PoS ou outros algoritmos.

## **Exemplo de Uso**

O código em `Blockchain.py` contém um exemplo de uso que demonstra como criar transações, minerar blocos e exibir a blockchain.

## **Relatório**

Um relatório mais detalhado sobre a implementação e as funcionalidades está disponível no arquivo `Relatório.md`

## **Licença**

Este projeto está licenciado sob a licença [MIT](https://choosealicense.com/licenses/mit/).












  


