import datetime
import hashlib
import json

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
        self.proximo_bloco = None

class Blockchain:
    def __init__(self, dificuldade=5):
        self.bloco_genesis = self.criar_bloco_genesis()
        self.ultimo_bloco = self.bloco_genesis
        self.transacoes_pendentes = []
        self.historico_transacoes = {}
        self.dificuldade = dificuldade
        self.saldos = {}  
        self.recompensa_minerador = 50  

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
        print(f"Bloco gênesis criado: {bloco_genesis.indice}.")
        return bloco_genesis

    def criar_bloco(self, prova, nonce, minerador):
        taxas_totais = sum(txn.get('Taxa', 0) for txn in self.transacoes_pendentes)
        self.transacoes_pendentes.append({
            'Remetente': 'Recompensa',
            'Destinatario': minerador,
            'Valor': self.recompensa_minerador + taxas_totais
        })

        novo_bloco = Bloco(
            indice=self.ultimo_bloco.indice + 1,
            timestamp=str(datetime.datetime.now()),
            transacoes=self.transacoes_pendentes,
            prova=prova,
            nonce=nonce,
            dificuldade=self.dificuldade,
            hash_anterior=self.ultimo_bloco.hash_atual
        )
        novo_bloco.hash_atual = self.gerar_hash(novo_bloco)
        self.transacoes_pendentes = []
        self.ultimo_bloco.proximo_bloco = novo_bloco
        self.ultimo_bloco = novo_bloco

        self.atualizar_saldos(novo_bloco)
        print(f"Bloco {novo_bloco.indice} criado e adicionado à blockchain com hash {novo_bloco.hash_atual}.")
        return novo_bloco

    def criar_transacao(self, remetente, destinatario, valor, taxa=0):
        if remetente != 'Recompensa' and self.saldos.get(remetente, 0) < valor + taxa:
            print("Erro: Saldo insuficiente.")
            return False

        transacao = {
            'Remetente': remetente,
            'Destinatario': destinatario,
            'Valor': valor,
            'Taxa': taxa
        }
        self.transacoes_pendentes.append(transacao)

        if remetente not in self.historico_transacoes:
            self.historico_transacoes[remetente] = []
        self.historico_transacoes[remetente].append(transacao)

        if destinatario not in self.historico_transacoes:
            self.historico_transacoes[destinatario] = []
        self.historico_transacoes[destinatario].append(transacao)

        print(f"Transação criada: {remetente} envia {valor} para {destinatario} com taxa {taxa}.")
        return self.ultimo_bloco.indice + 1

    def prova_de_trabalho(self, prova_anterior):
        nonce = 0
        prefixo_zeros = '0' * self.dificuldade
        print("Iniciando o Proof-of-Work...")

        while True:
            bloco_dados = f"{prova_anterior**2}{nonce}{self.dificuldade}"
            operacao_hash = hashlib.sha256(bloco_dados.encode()).hexdigest()

            if operacao_hash.startswith(prefixo_zeros):
                print(f"Proof-of-Work concluído: nonce={nonce}, hash={operacao_hash}")
                return nonce, operacao_hash
            nonce += 1

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

    def atualizar_saldos(self, bloco):
        for transacao in bloco.transacoes:
            remetente = transacao['Remetente']
            destinatario = transacao['Destinatario']
            valor = transacao['Valor']

            if remetente != 'Recompensa':
                self.saldos[remetente] = self.saldos.get(remetente, 0) - (valor + transacao.get('Taxa', 0))

            self.saldos[destinatario] = self.saldos.get(destinatario, 0) + valor

    def validar_cadeia(self):
        bloco_atual = self.bloco_genesis
        print("Iniciando a validação da blockchain...")

        while bloco_atual is not None:
            if bloco_atual.proximo_bloco:
                if bloco_atual.proximo_bloco.hash_anterior != bloco_atual.hash_atual:
                    print(f"Erro: Bloco {bloco_atual.indice} tem hash anterior inválido!")
                    return False

                prova_anterior = bloco_atual.prova
                operacao_hash = hashlib.sha256(f"{prova_anterior**2}".encode()).hexdigest()
                if not operacao_hash.startswith('0' * bloco_atual.proximo_bloco.dificuldade):
                    print(f"Erro: Bloco {bloco_atual.indice} tem prova de trabalho inválida!")
                    return False

            bloco_atual = bloco_atual.proximo_bloco

        print("Blockchain válida.")
        return True

    def exibir_cadeia(self):
        bloco_atual = self.bloco_genesis
        print("Blockchain atual:")

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
        print()

    def resolver_fork(self, cadeias):
        print("Resolvendo forks...")
        cadeia_mais_longa = max(cadeias, key=len)
        self.bloco_genesis = cadeia_mais_longa[0]
        self.ultimo_bloco = cadeia_mais_longa[-1]
        print("Fork resolvido: Adotada a cadeia mais longa.")
        self.recalcular_saldos()

    def recalcular_saldos(self):
        print("Recalculando saldos após resolver o fork...")
        self.saldos = {}
        bloco_atual = self.bloco_genesis

        while bloco_atual:
            self.atualizar_saldos(bloco_atual)
            bloco_atual = bloco_atual.proximo_bloco

    def propagar_transacao(self, transacao, nos):
        for no in nos:
            no.transacoes_pendentes.append(transacao)
        print("Transação propagada para todos os nós.")

    def propagar_bloco(self, bloco, nos):
        for no in nos:
            no.ultimo_bloco.proximo_bloco = bloco
            no.ultimo_bloco = bloco
        print("Bloco propagado para todos os nós.")

blockchain = Blockchain(dificuldade=4)
blockchain.saldos["Jennyfer"] = 500
blockchain.saldos["Gustavo"] = 200

blockchain.criar_transacao("Jennyfer", "Gustavo", 100, taxa=2)
blockchain.criar_transacao("Gustavo", "Maria", 50, taxa=1)

prova_anterior = blockchain.ultimo_bloco.prova
nonce, hash_atual = blockchain.prova_de_trabalho(prova_anterior)
blockchain.criar_bloco(prova_anterior, nonce, minerador="Minerador1")

blockchain.exibir_cadeia()
print("Saldos:", blockchain.saldos)