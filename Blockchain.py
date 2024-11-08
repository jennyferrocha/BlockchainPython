import datetime
import hashlib
import json

# Classe para representar um bloco
class Bloco:
    def __init__(self, indice, timestamp, transacoes, prova, nonce, dificuldade, hash_anterior):
        self.indice = indice
        self.timestamp = timestamp
        self.transacoes = transacoes
        self.prova = prova
        self.nonce = nonce
        self.dificuldade = dificuldade
        self.hash_anterior = hash_anterior
        self.hash_atual = None
        self.proximo_bloco = None  # Referência ao próximo bloco

# Classe para a Blockchain
class Blockchain:
    def __init__(self, dificuldade=5):  # Adiciona dificuldade como parâmetro opcional
        self.bloco_genesis = self.criar_bloco_genesis()
        self.ultimo_bloco = self.bloco_genesis  # Mantém a referência ao último bloco
        self.transacoes_pendentes = []  # Lista para transações pendentes
        self.historico_transacoes = {}  # Histórico de transações por endereço
        self.dificuldade = dificuldade  # Dificuldade inicial da prova de trabalho

    def criar_bloco_genesis(self):
        bloco_genesis = Bloco(
            indice=1,
            timestamp=str(datetime.datetime.now()),
            transacoes=[],
            prova=1,
            nonce=0,
            dificuldade=1,
            hash_anterior='0'
        )
        bloco_genesis.hash_atual = self.gerar_hash(bloco_genesis)
        print(f"Bloco gênesis criado: {bloco_genesis.indice}.\n")
        return bloco_genesis

    def criar_bloco(self, prova, nonce):
        # Calcula o nonce e o hash usando o sistema de Proof of Work
        nonce, hash_atual = self.prova_de_trabalho(prova)

        novo_bloco = Bloco(
            indice=self.ultimo_bloco.indice + 1,
            timestamp=str(datetime.datetime.now()),
            transacoes=self.transacoes_pendentes,
            prova=prova,
            nonce=nonce,
            dificuldade=self.dificuldade,
            hash_anterior=self.ultimo_bloco.hash_atual
        )
        novo_bloco.hash_atual = hash_atual
        self.transacoes_pendentes = []  # Limpa as transações pendentes
        self.ultimo_bloco.proximo_bloco = novo_bloco
        self.ultimo_bloco = novo_bloco  # Atualiza a referência para o último bloco

        print(f"Bloco {novo_bloco.indice} criado e adicionado à blockchain com hash {novo_bloco.hash_atual}.\n")
        return novo_bloco

    def criar_transacao(self, remetente, destinatario, valor):
        if not self.is_endereco_valido(remetente) or not self.is_endereco_valido(destinatario):
            print("Erro: Endereço inválido.\n")
            return False

        transacao = {
            'Remetente': remetente,
            'Destinatario': destinatario,
            'Valor': valor
        }
        self.transacoes_pendentes.append(transacao)

        if remetente not in self.historico_transacoes:
            self.historico_transacoes[remetente] = []
        self.historico_transacoes[remetente].append(transacao)

        if destinatario not in self.historico_transacoes:
            self.historico_transacoes[destinatario] = []
        self.historico_transacoes[destinatario].append(transacao)

        print(f"Transação criada: {remetente} envia {valor} para {destinatario}.\n")
        return self.ultimo_bloco.indice + 1

    def prova_de_trabalho(self, prova_anterior):
        nonce = 0
        prefixo_zeros = '0' * self.dificuldade
        print("Iniciando o Proof-of-Work...\n")

        while True:
            # Combina a prova, nonce e prova anterior para o cálculo do hash
            bloco_dados = f"{prova_anterior**2}{nonce}{self.dificuldade}"
            operacao_hash = hashlib.sha256(bloco_dados.encode()).hexdigest()

            # Verifica se o hash atende à dificuldade
            if operacao_hash.startswith(prefixo_zeros):
                print(f"Proof-of-Work concluído com sucesso: nonce={nonce}, hash={operacao_hash}\n")
                return nonce, operacao_hash
            nonce += 1  # Incrementa o nonce até encontrar um hash válido

    def gerar_hash(self, bloco):
        bloco_dados = {
            'indice': bloco.indice,
            'timestamp': bloco.timestamp,
            'transacoes': bloco.transacoes,
            'prova': bloco.prova,
            'nonce': bloco.nonce,
            'dificuldade': bloco.dificuldade,
            'hash_anterior': bloco.hash_anterior
        }
        bloco_codificado = json.dumps(bloco_dados, sort_keys=True).encode()
        return hashlib.sha256(bloco_codificado).hexdigest()

    def validar_cadeia(self):
        bloco_atual = self.bloco_genesis
        print("Iniciando a validação da blockchain...\n")

        while bloco_atual is not None:
            if bloco_atual.proximo_bloco:
                if bloco_atual.proximo_bloco.hash_anterior != bloco_atual.hash_atual:
                    print(f"Erro: O bloco {bloco_atual.indice} tem um hash anterior inválido!\n")
                    return False

                prova_anterior = bloco_atual.prova
                operacao_hash = hashlib.sha256(f"{prova_anterior**2}".encode()).hexdigest()
                if not operacao_hash.startswith('0' * bloco_atual.proximo_bloco.dificuldade):
                    print(f"Erro: O bloco {bloco_atual.indice} tem uma prova de trabalho inválida!\n")
                    return False

            bloco_atual = bloco_atual.proximo_bloco

        print("A blockchain é válida.\n")
        return True

    def exibir_cadeia(self):
        bloco_atual = self.bloco_genesis
        print("Blockchain atual:\n")

        while bloco_atual is not None:
            print(json.dumps({
                'indice': bloco_atual.indice,
                'timestamp': bloco_atual.timestamp,
                'transacoes': bloco_atual.transacoes,
                'prova': bloco_atual.prova,
                'nonce': bloco_atual.nonce,
                'dificuldade': bloco_atual.dificuldade,
                'hash_anterior': bloco_atual.hash_anterior,
                'hash_atual': bloco_atual.hash_atual
            }, indent=4))
            bloco_atual = bloco_atual.proximo_bloco
        print("\n")

    def exibir_historico_endereco(self, endereco):
        # Exibe o histórico de transações de um endereço
        if endereco in self.historico_transacoes:
            print(f"Histórico de transações para {endereco}:\n")
            for transacao in self.historico_transacoes[endereco]:
                print(json.dumps(transacao, indent=4))
            print("\n")
        else:
            print(f"Nenhuma transação encontrada para o endereço {endereco}.\n")

    def is_endereco_valido(self, endereco):
        return True

# Exemplo de uso:
blockchain = Blockchain(dificuldade=4)  # Ajusta a dificuldade desejada

# Criação de transações
blockchain.criar_transacao("Jennyfer", "Gustavo", "R$300,00")
blockchain.criar_transacao("Gustavo", "Maria", "R$60,00")

# Mineração de um novo bloco
prova_anterior = blockchain.ultimo_bloco.prova
nonce, hash_atual = blockchain.prova_de_trabalho(prova_anterior)
blockchain.criar_bloco(prova_anterior, nonce)

# Exibição do histórico de transações para um endereço específico
blockchain.exibir_historico_endereco("Jennyfer")
