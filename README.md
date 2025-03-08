# OSINTMaster Backend

**OSINTMaster Backend** é o motor de processamento para a coleção de ferramentas de **OSINT** (Open Source Intelligence) desenvolvidas para facilitar a coleta e análise de informações. Este backend fornece APIs e implementa a lógica para ferramentas como o **Scanner IP** e outras que serão adicionadas futuramente.

## 📦 Tecnologias Utilizadas

- **Framework**: Django
- **APIs**: Django REST Framework
- **Banco de Dados**: PostgreSQL (configurável)
- **Comunicação**: HTTP para servir o frontend OSINTMaster

## 🚀 Instalação

### Pré-requisitos

Antes de começar, verifique se você tem as seguintes dependências instaladas:

- [Python](https://www.python.org/) (recomendado 3.8+)
- [Django](https://www.djangoproject.com/)
- [Virtualenv](https://virtualenv.pypa.io/) (recomendado)

### Passos para Configuração

#### 1. Clonando o repositório

Clone o repositório em sua máquina local:

```bash
git clone https://github.com/LeviMaycon/osintmaster-backend.git
```

#### 2. Configurando o Ambiente Virtual

```bash
cd osintmaster-backend
python -m venv venv
```

Ative o ambiente virtual:

- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

#### 3. Instalando Dependências

```bash
pip install -r requirements.txt
```
#### 5. Configurando o Banco de Dados

```bash
python manage.py migrate
```

#### 6. Criando um Superusuário (opcional)

```bash
python manage.py createsuperuser
```

#### 7. Executando o Servidor

```bash
python manage.py runserver
```

O servidor estará disponível em `http://localhost:8000/`.

## 🛠️ APIs Disponíveis

### Scanner IP API

Endpoints da API para varredura de IP:

- `POST /api/scanner/ip/` - Iniciar nova varredura de IP

## 🔗 Integração com Frontend

Este backend foi projetado para se integrar com o [OSINTMaster Frontend](https://github.com/LeviMaycon/osintmaster-frontend). Configure as permissões CORS corretamente para permitir a comunicação.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

1. Fork o projeto
2. Crie sua branch de funcionalidade (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📞 Contato

Para dúvidas ou sugestões, entre em contato através de:
- Email: contato@osintmaster.com
- GitHub: [LeviMaycon](https://github.com/LeviMaycon)