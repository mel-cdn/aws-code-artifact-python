# AWS Code Artifact | Python

[![Build Status](https://github.com/mel-cdn/azure-fastapi-serverless/actions/workflows/deploy.yml/badge.svg?branch=main)](https://github.com/mel-cdn/azure-fastapi-serverless/actions/workflows/deploy.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Little project to explore pushing and pulling a Python libray to AWS Code Artifact

## Requirements

### Python

1. Install [pyenv](https://github.com/pyenv/pyenv#installation)
2. Install [Poetry](https://python-poetry.org/docs/)

### AWS

1. Setup AWS
2. Install [AWS CLI V2](https://aws.amazon.com/cli/)

## Setup the project

```bash
# Clone project
$ git clone https://github.com/mel-cdn/aws-code-artifact-python.git
$ cd aws-code-artifact-python

# Setup Python environment
$ pyenv install 3.12.3
$ poetry env use python3.12
$ poetry shell
$ poetry env info
$ poetry install

# Test Python environment
$ pytest --cov=shared
```

## Setup Code Artifact Domain and Repository

1. Create a domain if you don't have one yet. For console or CLI guide, see
   details [here](https://docs.aws.amazon.com/codeartifact/latest/ug/domain-create.html).
   <details>
   <summary>Domain (click to view)</summary>
   
   ![domain](images/domain.png)
   
   </details>


2. Create a repository under the domain. For console or CLI guide, see
   details [here](https://docs.aws.amazon.com/codeartifact/latest/ug/create-repo.html).
    <details>
    <summary>Repository (click to view)</summary>    

   ![repository](images/repository.png)

    </details>


3. Add [this policy](policies%2FCodeArtifactDeployer.json) to your AWS account or service account to be able to
   interact (**publish** and **pull**) with the repository.

## Publish private Python module to Repository

## Install private Python module to your environment