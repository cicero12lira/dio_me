---

# Simulação de Sistema Bancário em Python

Este projeto implementa uma simulação simples de um sistema bancário em Python. Ele permite que usuários realizem operações básicas como depósitos, saques e consultas de saldo. O sistema também impõe restrições para garantir que as operações financeiras sejam válidas.

## Funcionalidades

### 1. **Depósito**
   - O método `depositar()` permite que o usuário adicione fundos à sua conta.
   - O sistema garante que apenas valores positivos possam ser depositados.
   - Após o depósito, o saldo é atualizado e uma mensagem de confirmação é exibida.

### 2. **Saque**
   - O método `sacar()` permite que o usuário retire fundos de sua conta, com diversas validações:
     - **Valor positivo**: Saques de valores negativos ou zero não são permitidos.
     - **Limite de saque**: Há um limite máximo de saque por dia, que é controlado e acumulado com base nos saques realizados.
     - **Saldo suficiente**: O sistema verifica se o saldo da conta é suficiente para cobrir o saque solicitado.
   - Se todas as condições forem atendidas, o saldo é debitado e o usuário recebe uma confirmação. O sistema também exibe o total sacado no dia e o limite restante disponível.

### 3. **Consulta de Saldo**
   - O método `consultar_saldo()` exibe o saldo atual da conta.

### 4. **Menu de Interação**
   - O sistema possui um menu interativo que permite ao usuário escolher entre as operações de depósito, saque, consulta de saldo ou saída do sistema.
   - O menu é apresentado em loop até que o usuário decida sair do programa.

### 5. **Continuação e Saída**
   - O sistema permite que o usuário decida se deseja continuar realizando operações ou sair do programa após cada transação.
   - A opção de sair encerra o programa de maneira segura.

## Exemplo de Uso

Ao iniciar o programa, o usuário pode interagir com o menu para realizar diferentes operações:

```plaintext
########### Menu #############

        [d]epositar
        [s]acar
        [e]xtrato
        [ss]air

###############################

-> 
```

Dependendo da escolha do usuário, o sistema processará a operação correspondente e exibirá os resultados ou mensagens de erro conforme necessário.

## Requisitos

- Python 3.x

## Como Executar

1. Clone este repositório para sua máquina local.
2. Execute o script Python usando o comando:

   ```bash
   python banco.py
   ```

3. Siga as instruções no menu para realizar depósitos, saques ou consultar o saldo.

## Observações

- O valor máximo de saque por dia é definido pelo parâmetro `limite_saque` na classe `Banco`, com um valor padrão de R$1000,00.
- O saldo inicial também pode ser configurado ao instanciar a classe `Banco`.

---

