# Gerenciador Financeiro

## 🔹 Requisitos Funcionais Atualizados

### 1. Cadastro de Transações
O usuário pode adicionar manualmente:
- **Dívidas** (parceladas ou à vista)
- **Recebimentos** (salário, rendas extras, bônus, etc.)
- **Gastos fixos** (aluguéis, contas, assinaturas)
- **Investimentos** (como poupança, CDB, ações, etc.)

Para investimentos:
- Funcionam como dívidas, mas o usuário define o valor que deseja aplicar.
- Podem ser recorrentes (mensais, quinzenais, semanais) ou eventuais.

### 2. Débito Automático e Parcelamentos
- Compras no cartão de crédito são automaticamente registradas como dívidas parceladas.
- Parcelamentos permitem:
  - Pagamento antecipado
  - Adiamento para o próximo mês
  - Parcelamento duplicado (parte da dívida adicionada ao próximo ciclo)

### 3. Gestão de Orçamento e Gastos
- **Definir saldo disponível:**
  - O usuário informa o valor disponível no início do mês/quinzena.
- **Desconto de gastos fixos:**
  - No início de cada quinzena, os gastos fixos são subtraídos automaticamente.
- **Cálculo de orçamento flexível:**
  - **Valor diário** = (saldo restante após gastos fixos) ÷ dias restantes da quinzena
  - **Valor semanal** = (saldo restante após gastos fixos) ÷ semanas restantes do mês
  - O usuário pode ajustar manualmente os valores para priorizar certos períodos.

### 4. Status das Dívidas e Investimentos
Cada transação pode ter status como:
- **Paga**
- **Pendente**
- **Atrasada**
- **Adiada**
- **Parcela duplicada**

Para investimentos:
- **Ativo:** o investimento continua sendo feito
- **Pausado:** temporariamente suspenso
- **Finalizado:** atingiu o valor desejado

### 5. Relatórios e Alertas
- **Resumo financeiro quinzenal e mensal:**
  - Quanto já foi gasto
  - Quanto ainda pode ser gasto
  - Percentual destinado a investimentos
- **Notificações e lembretes:**
  - Avisos de vencimento de dívidas
  - Alerta quando o orçamento diário/semanal estiver se esgotando
- **Gráficos de evolução financeira:**
  - Comparação de gastos entre meses
  - Análise de distribuição entre dívidas, investimentos e despesas variáveis

### 6. Referência
- [Organizze](https://app.organizze.com.br/)

## 🔹 Entidades e Relacionamentos

### Usuário (users)
| Campo         | Tipo       | Descrição                        |
|--------------|-----------|--------------------------------|
| id_user (PK) | INT       | Identificador único do usuário |
| nome         | VARCHAR   | Nome do usuário                |
| email        | VARCHAR   | Email do usuário               |
| senha        | VARCHAR   | Senha criptografada            |
| data_criacao | DATE      | Data de criação da conta       |

### Contas Bancárias (accounts)
| Campo         | Tipo       | Descrição                                |
|--------------|-----------|----------------------------------------|
| id_account (PK) | INT   | Identificador único da conta          |
| id_user (FK)  | INT   | Referência ao usuário dono da conta    |
| nome_banco    | VARCHAR | Nome do banco (ex: Nubank)            |
| saldo         | FLOAT   | Saldo disponível na conta              |
| tipo_conta    | VARCHAR | Tipo da conta (ex: carteira, corrente, poupança) |

### Transações (transactions)
| Campo            | Tipo       | Descrição                                |
|----------------|-----------|----------------------------------------|
| id_transaction (PK) | INT   | Identificador único da transação     |
| id_account (FK) | INT   | Referência à conta bancária          |
| tipo           | VARCHAR | Tipo da transação (receita, despesa ou transferência) |
| valor         | FLOAT   | Valor da transação                     |
| categoria     | VARCHAR | Categoria da transação (ex: alimentação, transporte) |
| data_transacao | DATE   | Data em que a transação ocorreu       |

### Gastos Fixos (fixed_expenses)
| Campo             | Tipo       | Descrição                       |
|-----------------|-----------|---------------------------------|
| id_fixed_expense (PK) | INT | Identificador único            |
| id_user (FK)    | INT       | Referência ao usuário           |
| descricao       | VARCHAR   | Descrição do gasto fixo         |
| valor          | FLOAT     | Valor do gasto                  |
| vencimento     | DATE      | Data de vencimento              |
| status         | VARCHAR   | Se o pagamento foi realizado ou não |

### Dívidas e Parcelamentos (debts)
| Campo         | Tipo       | Descrição                        |
|--------------|-----------|--------------------------------|
| id_debt (PK) | INT       | Identificador único da dívida  |
| id_user (FK) | INT       | Referência ao usuário         |
| descricao    | VARCHAR   | Descrição da dívida           |
| valor_total  | FLOAT     | Valor total da dívida         |
| parcelas     | INT       | Número de parcelas           |
| valor_parcela | FLOAT    | Valor de cada parcela        |
| vencimento   | DATE      | Data do vencimento da próxima parcela |
| status       | VARCHAR   | Pago, pendente ou adiado     |

### Investimentos (investments)
| Campo            | Tipo       | Descrição                        |
|----------------|-----------|--------------------------------|
| id_investment (PK) | INT  | Identificador único do investimento |
| id_user (FK)  | INT       | Referência ao usuário         |
| descricao     | VARCHAR   | Descrição do investimento    |
| valor_aplicado | FLOAT   | Valor investido             |
| data_aplicacao | DATE    | Data da aplicação           |
| tipo_investimento | VARCHAR | Tipo (ex: renda fixa, variável) |

---
📌 **Este documento descreve os requisitos funcionais e estrutura do banco de dados para um gerenciador financeiro.**

