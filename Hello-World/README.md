# Hello World: Python to Azure App Service with Azure DevOps YAML

This repository contains a small Flask application, tests, and a two-stage Azure DevOps pipeline that builds, tests, packages, and deploys the app to an existing Linux Azure App Service.

## Repository structure

```text
.
├── app.py
├── requirements.txt
├── requirements-dev.txt
├── tests/
│   └── test_app.py
├── azure-pipelines.yml
└── .gitignore
```

## 1. Create the Azure resources

Create a **Linux Web App** in Azure App Service and select Python 3.11 as the runtime. Record:

- Azure subscription
- Resource group name
- App Service name

The pipeline assumes the App Service already exists.

## 2. Create the Azure DevOps service connection

In Azure DevOps:

1. Open **Project settings**.
2. Select **Service connections**.
3. Select **New service connection**.
4. Choose **Azure Resource Manager**.
5. Create the connection and grant it access to the subscription or resource group containing the App Service.
6. Record the service connection name.

## 3. Update pipeline placeholders

Edit `azure-pipelines.yml` and replace:

- `REPLACE-WITH-SERVICE-CONNECTION`
- `REPLACE-WITH-APP-SERVICE-NAME`
- `REPLACE-WITH-RESOURCE-GROUP`

## 4. Push to Azure Repos

```bash
git init
git add .
git commit -m "Add Python Hello World App Service pipeline"
git branch -M main
git remote add origin <YOUR-AZURE-REPOS-GIT-URL>
git push -u origin main
```

## 5. Create and run the pipeline

1. Open **Pipelines** in Azure DevOps.
2. Select **New pipeline**.
3. Select **Azure Repos Git** and this repository.
4. Select **Existing Azure Pipelines YAML file**.
5. Select `/azure-pipelines.yml`.
6. Save and run.
7. Authorize the service connection if Azure DevOps requests permission.

## 6. Test the deployment

Open:

```text
https://<APP-SERVICE-NAME>.azurewebsites.net/
https://<APP-SERVICE-NAME>.azurewebsites.net/health
```

Expected root response:

```text
Hello World from Python on Azure App Service!
```

Expected health response:

```json
{"status":"healthy"}
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -q
python app.py
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Then browse to `http://localhost:8000`.
