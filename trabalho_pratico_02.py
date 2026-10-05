from datetime import date


class Veiculo:
    def __init__(self, placa, modelo, ano, valor_diaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.manutencoes = []

    def calcular_valor(self, dias):
        return self.valor_diaria * dias

    def adicionar_manutencao(self, manutencao):
        self.manutencoes.append(manutencao)

    def mostrar_dados(self):
        return f"{self.modelo} - Placa: {self.placa} - Ano: {self.ano}"


class Carro(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, portas):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.portas = portas

    def mostrar_tipo(self):
        return f"Carro com {self.portas} portas"


class Moto(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, cilindradas):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.cilindradas = cilindradas

    def mostrar_tipo(self):
        return f"Moto com {self.cilindradas} cilindradas"


class Caminhao(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, capacidade):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.capacidade = capacidade

    def mostrar_tipo(self):
        return f"Caminhão com capacidade de {self.capacidade} toneladas"


class Cliente:
    def __init__(self, nome, documento, telefone):
        self.nome = nome
        self.documento = documento
        self.telefone = telefone
        self.contratos = []

    def adicionar_contrato(self, contrato):
        self.contratos.append(contrato)

    def mostrar_dados(self):
        return f"{self.nome} - Documento: {self.documento}"


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)
        self.cpf = cpf

    def tipo_cliente(self):
        return "Pessoa Física"


class PessoaJuridica(Cliente):
    def __init__(self, razao_social, cnpj, telefone):
        super().__init__(razao_social, cnpj, telefone)
        self.cnpj = cnpj

    def tipo_cliente(self):
        return "Pessoa Jurídica"


class Condutor:
    def __init__(self, nome, cnh):
        self.nome = nome
        self.cnh = cnh
        self.contrato = None

    def vincular_contrato(self, contrato):
        self.contrato = contrato

    def mostrar_dados(self):
        return f"{self.nome} - CNH: {self.cnh}"


class Manutencao:
    def __init__(self, data, tipo_servico, custo):
        self.data = data
        self.tipo_servico = tipo_servico
        self.custo = custo

    def mostrar_dados(self):
        return f"{self.data} - {self.tipo_servico} - R$ {self.custo:.2f}"

    def alterar_custo(self, novo_custo):
        self.custo = novo_custo


class Contrato:
    def __init__(
        self,
        data_inicio,
        data_termino,
        cliente,
        veiculo,
        condutor
    ):
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.cliente = cliente
        self.veiculo = veiculo
        self.condutor = condutor
        self.valor_total = 0
        self.status = "ativo"

        self.cliente.adicionar_contrato(self)
        self.condutor.vincular_contrato(self)

    def calcular_valor(self):
        dias = (self.data_termino - self.data_inicio).days

        if dias <= 0:
            dias = 1

        self.valor_total = self.veiculo.calcular_valor(dias)
        return self.valor_total

    def finalizar(self):
        self.status = "finalizado"

    def cancelar(self):
        self.status = "cancelado"

    def mostrar_contrato(self):
        print("\n===== CONTRATO DE LOCAÇÃO =====")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Veículo: {self.veiculo.modelo}")
        print(f"Placa: {self.veiculo.placa}")
        print(f"Condutor: {self.condutor.nome}")
        print(f"Início: {self.data_inicio}")
        print(f"Término: {self.data_termino}")
        print(f"Valor total: R$ {self.valor_total:.2f}")
        print(f"Status: {self.status}")


if __name__ == "__main__":

    cliente = PessoaFisica(
        "Carlos Eduardo",
        "12345678901",
        "(86) 99999-9999"
    )

    veiculo = Carro(
        "ABC1D23",
        "Toyota Corolla",
        2024,
        180.00,
        4
    )

    manutencao = Manutencao(
        date(2026, 10, 1),
        "Troca de óleo",
        350.00
    )

    veiculo.adicionar_manutencao(manutencao)

    condutor = Condutor(
        "Carlos Eduardo",
        "12345678900"
    )

    contrato = Contrato(
        date(2026, 10, 5),
        date(2026, 10, 8),
        cliente,
        veiculo,
        condutor
    )

    contrato.calcular_valor()

    print("===================================")
    print("SISTEMA DE LOCAÇÃO DE VEÍCULOS")
    print("===================================")

    print("\nDados do cliente:")
    print(cliente.mostrar_dados())
    print(cliente.tipo_cliente())

    print("\nDados do veículo:")
    print(veiculo.mostrar_dados())
    print(veiculo.mostrar_tipo())

    print("\nManutenção:")
    print(manutencao.mostrar_dados())

    contrato.mostrar_contrato()