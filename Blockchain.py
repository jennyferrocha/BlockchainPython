import datetime
import hashlib
import json

# Classe para representar um bloco 
class Bloco:
    def __init__(self, indice, timestamp, transacoes, prova, hash_anterior):
        self.indice = indice
        self.timestamp = timestamp
        self.transacoes = transacoes
        self.prova = prova
        self.hash_anterior = hash_anterior
        self.hash_atual = None
        self.proximo_bloco = None  # Referência ao próximo bloco 

# Classe para a Blockchain
class Blockchain:
    def __init__(self):
        self.bloco_genesis = self.criar_bloco_genesis()
        self.ultimo_bloco = self.bloco_genesis  # Mantém a referência ao último bloco
        self.transacoes_pendentes = []  # Lista para transações pendentes

    def criar_bloco_genesis(self):
        # Cria o bloco gênesis (primeiro bloco da blockchain)
        bloco_genesis = Bloco(indice=1, 
                              timestamp=str(datetime.datetime.now()), 
                              transacoes=[], 
                              prova=1, 
                              hash_anterior='0')
        bloco_genesis.hash_atual = self.gerar_hash(bloco_genesis)
        print(f"Bloco gênese criado: {bloco_genesis.indice}.\n")
        return bloco_genesis

    def criar_bloco(self, prova):
        # Cria um novo bloco e adiciona à blockchain
        novo_bloco = Bloco(
            indice=self.ultimo_bloco.indice + 1,
            timestamp=str(datetime.datetime.now()),
            transacoes=self.transacoes_pendentes,
            prova=prova,
            hash_anterior=self.ultimo_bloco.hash_atual
        )
        novo_bloco.hash_atual = self.gerar_hash(novo_bloco)
        self.transacoes_pendentes = []  # Limpa as transações pendentes

        # Encadeia o bloco anterior ao novo
        self.ultimo_bloco.proximo_bloco = novo_bloco
        self.ultimo_bloco = novo_bloco  # Atualiza a referência para o último bloco

        print(f"Bloco {novo_bloco.indice} criado e adicionado à blockchain.\n")
        return novo_bloco

    def criar_transacao(self, remetente, destinatario, valor):
        # Cria uma nova transação
        transacao = {
            'Remetente': remetente,
            'Destinatario': destinatario,
            'Valor': valor
        }
        self.transacoes_pendentes.append(transacao)
        print(f"Transação criada: {remetente} envia {valor} para {destinatario}.\n")
        return self.ultimo_bloco.indice + 1

    def prova_de_trabalho(self, prova_anterior):
        nova_prova = 1
        prova_valida = False
        print("Iniciando o Proof-of-Work...\n")
        while not prova_valida:
            operacao_hash = hashlib.sha256(str(nova_prova**2 - prova_anterior**2).encode()).hexdigest()
            if operacao_hash[:4] == '0000':  # Validação da prova de trabalho
                prova_valida = True
            else:
                nova_prova += 1
        print(f"Proof-of-Work concluído com sucesso: {nova_prova}.\n")
        return nova_prova

    def gerar_hash(self, bloco):
        bloco_dados = {
            'indice': bloco.indice,
            'timestamp': bloco.timestamp,
            'transacoes': bloco.transacoes,
            'prova': bloco.prova,
            'hash_anterior': bloco.hash_anterior
        }
        bloco_codificado = json.dumps(bloco_dados, sort_keys=True).encode()
        return hashlib.sha256(bloco_codificado).hexdigest()

    def validar_cadeia(self):
        bloco_atual = self.bloco_genesis
        print("Iniciando a validação da blockchain...\n")

        while bloco_atual is not None:
            if bloco_atual.proximo_bloco:
                # Verifica se o hash do bloco atual é igual ao hash_anterior do próximo bloco
                if bloco_atual.proximo_bloco.hash_anterior != bloco_atual.hash_atual:
                    print(f"Erro: O bloco {bloco_atual.indice} tem um hash anterior inválido!\n")
                    return False

                # Verifica se a prova de trabalho é válida
                prova_anterior = bloco_atual.prova
                prova_atual = bloco_atual.proximo_bloco.prova
                operacao_hash = hashlib.sha256(str(prova_atual**2 - prova_anterior**2).encode()).hexdigest()
                if operacao_hash[:4] != '0000':
                    print(f"Erro: O bloco {bloco_atual.indice} tem uma prova de trabalho inválida!\n")
                    return False

            bloco_atual = bloco_atual.proximo_bloco

        print("A blockchain é válida.\n")
        return True

    def exibir_cadeia(self):
        # Exibe a blockchain completa
        bloco_atual = self.bloco_genesis
        print("Blockchain atual:\n")

        while bloco_atual is not None:
            print(json.dumps({
                'indice': bloco_atual.indice,
                'timestamp': bloco_atual.timestamp,
                'transacoes': bloco_atual.transacoes,
                'prova': bloco_atual.prova,
                'hash_anterior': bloco_atual.hash_anterior,
                'hash_atual': bloco_atual.hash_atual
            }, indent=4))
            bloco_atual = bloco_atual.proximo_bloco
        print("\n")

# Exemplo de uso:
blockchain = Blockchain()

# Criação de transações
blockchain.criar_transacao("Jennyfer", "Gustavo", "R$300,00")
blockchain.criar_transacao("Gustavo", "Maria", "R$60,00")

# Mineração de um novo bloco
prova_anterior = blockchain.ultimo_bloco.prova
prova = blockchain.prova_de_trabalho(prova_anterior)
blockchain.criar_bloco(prova)

# Validação da blockchain
blockchain.validar_cadeia()

# Exibição da blockchain
blockchain.exibir_cadeia()
