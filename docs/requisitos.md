# Requisitos

## Requisitos funcionais

| ID | Requisito |
| --- | --- |
| RF01 |  O sistema deve listar as disciplinas disponíveis, mostrando o número de vagas restantes de cada uma. |
| RF02 | O sistema deve identificar o aluno pelo número de matrícula antes de permitir qualquer operação. |
| RF03 | O sistema deve permitir que o aluno se matricule em uma disciplina (fluxo principal) |
| RF04 | O sistema deve validar a matrícula, recusando-a quando não houver vagas ou quando o aluno já estiver matriculado na disciplina, e informar o motivo.
| RF05 | O sistema deve permitir que o aluno consulte as disciplinas em que está matriculado. |

## Requisitos não funcionais

| ID | Requisito |
| --- | --- |
| RNF01 | O sistema deve seguir a arquitetura em 3 camadas (apresentação, negócio e dados): a tela só se comunica com a camada de negócio, e somente a camada de negócio acessa o banco de dados. |
| RNF02 |  |
| RNF03 |  |
