# **Relatório da Implementação da Blockchain Simulada**

Este relatório descreve a implementação de uma Blockchain Simplificada em Python, com foco nos seguintes aspectos:

- **Propagação de Blocos e Transações:** Simulação da disseminação de informações na rede.
- **Resolução de Conflitos (Forks):** Mecanismo para lidar com conflitos na cadeia.
- **Estado Global e Controle de Saldos:** Gerenciamento dos saldos de cada endereço.
- **Taxas de Transação e Recompensas:** Incentivos para mineradores.

### **1. Propagação de Blocos e Transações**

As funções `propagar_transacao()` e `propagar_bloco()` simulam a propagação, adicionando a transação/bloco a todos os nós na lista `nos`.

```python
    def propagar_transacao(self, transacao, nos):
        # ... (código da função)

    def propagar_bloco(self, bloco, nos):
       # ... (código da função)
```

**Limitações:**  Esta é uma simulação. Uma implementação real usaria protocolos de rede.

### **2. Resolução de Conflitos (Forks)**

A função `resolver_fork()` escolhe a cadeia mais longa e `recalcular_saldos()` garante a consistência.

```python
    def resolver_fork(self, cadeias):
        # ... (código da função)

    def recalcular_saldos(self):
        # ... (código da função)
```

**Limitações:** A simulação de forks é simplificada.

### **3. Estado Global e Controle de Saldos**

O dicionário `self.saldos` guarda os saldos. `criar_transacao()` verifica saldos antes de autorizar transações, e `atualizar_saldos()` atualiza os saldos após a mineração.

```python
    def atualizar_saldos(self, bloco):
        # ... (código da função)
```

### **4. Taxas de Transação e Recompensas**

As transações têm um campo `taxa`. `criar_bloco()` soma as taxas à recompensa do minerador.

```python
    def criar_bloco(self, prova, nonce, minerador):
        # ... (código da função)
```

## **Arquitetura da Blockchain**

A blockchain é composta por uma série de blocos encadeados. Cada bloco contém:

* **Índice:** Posição do bloco na cadeia.
* **Timestamp:** Data e hora de criação.
* **Transações:** Lista de transações incluídas no bloco.
* **Prova:** Resultado do Proof-of-Work.
* **Nonce:** Número usado no PoW.
* **Hash Anterior:** Hash do bloco anterior.
* **Hash Atual:** Hash do bloco atual.

## **Proof-of-Work (PoW):**

O algoritmo PoW simplificado busca um `nonce` que, ao ser hasheado com a prova anterior, gere um hash com um número específico de zeros iniciais.  A dificuldade do PoW é ajustada pelo parâmetro `dificuldade`.

## **Considerações Finais**

Este projeto é didático e não se destina a produção.  Segurança, persistência e consenso são simplificados. A simulação oferece uma visão básica, mas não reflete a complexidade de um sistema real.

## **Licença**

Este projeto está licenciado sob a licença [MIT](https://choosealicense.com/licenses/mit/).