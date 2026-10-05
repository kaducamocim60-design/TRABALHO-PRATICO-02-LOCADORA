# Trabalho Prático 02 — Sistema de Gerenciamento de uma Locadora de Veículos

## Sobre o trabalho

Este trabalho apresenta a modelagem de um sistema para uma locadora de veículos.

A proposta é organizar as informações relacionadas aos veículos disponíveis para locação, aos clientes, aos contratos, aos condutores e às manutenções realizadas nos veículos.

Durante a elaboração do trabalho foram utilizados conceitos de Programação Orientada a Objetos, principalmente classes, objetos, herança, associação e composição.

---

## 1. Classes identificadas

A partir do estudo de caso, foram identificadas as seguintes classes:

### Veículos

* `Veiculo`
* `Carro`
* `Moto`
* `Caminhao`

A classe `Veiculo` representa as características que são comuns aos diferentes veículos da locadora, como placa, modelo, ano e valor da diária.

As classes `Carro`, `Moto` e `Caminhao` representam tipos específicos de veículos.

### Clientes

* `Cliente`
* `PessoaFisica`
* `PessoaJuridica`

A classe `Cliente` possui as informações comuns aos clientes da locadora.

A partir dela foram criadas as especializações `PessoaFisica` e `PessoaJuridica`.

### Outras classes

* `Contrato`
* `Condutor`
* `Manutencao`

A classe `Contrato` representa o aluguel realizado pelo cliente.

A classe `Condutor` representa a pessoa responsável por conduzir o veículo durante aquele contrato.

A classe `Manutencao` representa os serviços realizados nos veículos ao longo do tempo.

---

## 2. Herança

Foi utilizada herança em duas partes do sistema.

### Veículos

A classe `Veiculo` é a superclasse de:

* `Carro`
* `Moto`
* `Caminhao`

Isso acontece porque carro, moto e caminhão são tipos diferentes de veículos, mas possuem algumas informações em comum.

Por exemplo, todos possuem placa, modelo, ano e valor da diária.

### Clientes

A classe `Cliente` é a superclasse de:

* `PessoaFisica`
* `PessoaJuridica`

Nesse caso, os dois tipos de clientes possuem informações básicas em comum, como nome ou razão social, documento e telefone.

---

## 3. Relacionamentos entre as classes

### Cliente e Contrato

**Tipo: Associação**

Um cliente pode realizar vários contratos de locação durante sua utilização dos serviços da empresa.

Cada contrato, por sua vez, pertence a um único cliente.

---

### Veiculo e Contrato

**Tipo: Associação**

Um veículo pode participar de diferentes contratos ao longo do tempo.

Porém, de acordo com o estudo de caso, um mesmo veículo não pode estar em dois contratos ativos ao mesmo tempo.

---

### Contrato e Condutor

**Tipo: Composição**

O condutor está diretamente relacionado ao contrato de locação.

Ele é cadastrado no momento da locação e existe dentro do contexto daquele contrato. Se o contrato deixar de existir, o condutor não possui motivo para continuar existindo isoladamente no sistema.

Por isso, esse relacionamento foi classificado como composição.

---

### Veiculo e Manutencao

**Tipo: Composição**

Um veículo pode possuir várias manutenções durante sua utilização.

Cada manutenção pertence a um único veículo e faz parte do seu histórico.

Por esse motivo, o relacionamento foi representado como composição.

---

## 4. Implementação em Python

A implementação parcial foi realizada no arquivo:

`trabalho_pratico_02.py`

Foi utilizada a linguagem Python para demonstrar os relacionamentos entre os objetos.

Um exemplo é a criação de uma manutenção e sua associação com um veículo:

```python
manutencao = Manutencao(
    date(2026, 10, 1),
    "Troca de óleo",
    350.00
)

veiculo.adicionar_manutencao(manutencao)
```

Nesse exemplo, a manutenção é criada e depois associada ao veículo.

Também foi demonstrado o relacionamento entre contrato e condutor:

```python
contrato = Contrato(
    date(2026, 10, 5),
    date(2026, 10, 8),
    cliente,
    veiculo,
    condutor
)
```

Assim, o contrato recebe os objetos relacionados ao cliente, ao veículo e ao condutor.

---

## 5. Estrutura do projeto

O projeto está organizado da seguinte maneira:

```text
TRABALHO-PRATICO-02-LOCADORA
│
├── README.md
├── UML.jpeg
└── trabalho_pratico_02.py
```

### README.md

Contém a explicação do estudo de caso, das classes, da herança, dos relacionamentos e da implementação.

### UML.jpeg

Contém o diagrama UML elaborado para representar visualmente as classes e seus relacionamentos.

### trabalho_pratico_02.py

Contém a implementação parcial do sistema em Python.

---

## 6. Tecnologias utilizadas

* Python
* Programação Orientada a Objetos
* UML
* Git
* GitHub

---

## 7. Conclusão

O desenvolvimento deste trabalho permitiu representar, de forma orientada a objetos, as principais partes de um sistema de gerenciamento de uma locadora de veículos.

Através da modelagem foi possível identificar classes, atributos, métodos, especializações e diferentes tipos de relacionamento entre os objetos.

A implementação em Python demonstra na prática como essas classes podem ser criadas e relacionadas dentro de um sistema.
