# 🐷 Porquinho Bank

Bem-vindo ao **Porquinho Bank** — o banco mais fofo e desastrado do Python! 🏦✨  
Um simples sistema bancário feito em **Python** com funcionalidades básicas de **depósito**, **saque** e **extrato**, tudo pelo terminal.  
Ideal para praticar **lógica de programação**, **controle de fluxo** e **manipulação de variáveis**.

---

## 💡 Funcionalidades

- 💰 **Depósito** — permite adicionar valores positivos ao saldo.  
- 💸 **Saque** — realiza saques com:
  - Limite máximo de R$500,00 por operação.
  - Até **3 saques diários**.
  - Verificação automática de saldo insuficiente.
- 🧾 **Extrato** — exibe o histórico completo de depósitos e saques realizados.  
- 🚪 **Sair** — encerra o programa com uma mensagem personalizada.

---

## 🧠 Lógica do Programa

O sistema funciona em **loop**, exibindo um menu principal:

--- 


Cada opção aciona uma parte da lógica:

- `1` → Solicita um valor para depósito (somente positivo).  
- `2` → Verifica limite, número de saques e saldo antes de sacar.  
- `3` → Mostra o extrato formatado.  
- `0` → Finaliza a execução do programa.

---

## ⚙️ Tecnologias Utilizadas

- 🐍 **Python 3.x**
- 🧩 Nenhuma biblioteca externa — apenas recursos nativos da linguagem.

---

## 🚀 Como Executar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/seu-usuario/porquinho-bank.git
   cd porquinho-bank
   
2. **Execute o Script:**
   ```bash
   python porquinho_bank.py
   
3. **Interaja com o Menu e divirta-se!**

---

## 📚 Aprendizados Envolvidos

Estruturas condicionais `(if / elif / else)`

Laços de repetição `(while)`

Manipulação de strings e variáveis

Controle de fluxo e tratamento de erros lógicos

Simulação de um sistema bancário simples
