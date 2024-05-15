# TRABALHO DE REDES
## ALUNOS: JOÃO VICTOR DE OLIVEIRA COSTA, VÍTOR VIANA DA SILVA
## PROFESSOR: FLÁVIO

SISTEMA DE ENVIO DE EMAILS

Este projeto tem como finalidade o envio de e-mail através de um formulário HTML que faz uma requisição HTTP
para uma aplicação web service responsável pelo envio de e-mail via SMTP.
Este sistema foi dividido em dois módulos principais: o frontend, que é aplicação cliente,
e o backend, que é a aplicação servidor.

Aplicação Cliente
Esta camada do projeto é responsável por obter informações do usuario, como email de destino, o título do e-mail e a mensagem
que será enviada, para o back end que está em local host na porta 8000.

Aplicação Servidor 
A aplicação servidor foi construída utilizando a linguagem Python, o framework FastAPI e o servidor Uvicorn, que é um servidor
para rodar aplicações assíncronas em Python.

O fastapi é responsável por receber as informações enviadas pelo cliente através do formulario, via HTTP, e pelo envio dos
e-mails via SMTP.
A arquitetura em camadas é a que está sendo utilizada para a organização do projeto.
O projeto foi dividido em três camadas: configuração, controle e serviço.
A camada de configuração é responsável por pegar as infomações necessárias para estabelecer uma conexão SMTP.
Já na camada de controle é responsavel por pegar as informações do formulario se conectar com a camada de serviço.
Por fim, na camada de serviço é responsavel por pegar as informações da camada de controle e estabelecer uma conexão 
com o servidor SMTP do gmail e enviar o email solicitado pelo usuário.

PRÉ-REQUISITOS
É necessário possuir Python, FastAPI e o Uvicorn.

INSTRUÇÕES DE INSTALAÇÃO
É necessário possuir o Python e o pip na máquina. Para gerenciar os pacotes do Python, o processo de instalação do FastAPI e do Uvicorn através do pip, serão necessários os seguintes comandos:É necessário possuir o python e pip na máquina, gerenciar de pacotes do python, o processo de intalação do fastapi e o uvicorn
 atraves do pip será necessário os seguintes comandos.

 pip install fastapi
 pip install uvicorn

AUTORIA E CONTRIBUIÇÕES
João Victor e Vítor Viana.
Para a criação deste projeto, foi utilizada a documentação do FastAPI. Segue o link: 
 https://fastapi.tiangolo.com/
